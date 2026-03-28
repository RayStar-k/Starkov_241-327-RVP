from flask import Flask, request, render_template, redirect, url_for, make_response
from werkzeug.middleware.proxy_fix import ProxyFix
import re

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

app.config['APPLICATION_ROOT'] = '/rvp/lab2'
app.config['PREFERRED_URL_SCHEME'] = 'https'

app.wsgi_app = ProxyFix(app.wsgi_app, x_prefix=1)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/request-info')
def request_info():
    url_params = request.args.to_dict()
    headers = dict(request.headers)
    cookies = request.cookies.to_dict()

    return render_template('request_info.html',
                         url_params=url_params,
                         headers=headers,
                         cookies=cookies)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        remember = request.form.get('remember', '')

        return render_template('login_result.html',
                             username=username,
                             password=password,
                             remember=remember,
                             form_data=request.form.to_dict())

    return render_template('login.html')


@app.route('/phone', methods=['GET', 'POST'])
def phone():
    error = None
    formatted_phone = None
    phone_input = ''

    if request.method == 'POST':
        phone_input = request.form.get('phone', '').strip()

        is_valid, error_msg, formatted = validate_phone(phone_input)

        if is_valid:
            formatted_phone = formatted
        else:
            error = error_msg

    return render_template('phone.html',
                         error=error,
                         formatted_phone=formatted_phone,
                         phone_input=phone_input)


def validate_phone(phone):
    if not phone:
        return False, 'Недопустимый ввод. В номере телефона встречаются недопустимые символы.', None

    allowed_pattern = r'^[\d\s()\-\.+]+$'

    if not re.match(allowed_pattern, phone):
        return False, 'Недопустимый ввод. В номере телефона встречаются недопустимые символы.', None

    digits = re.sub(r'\D', '', phone)
    digit_count = len(digits)

    starts_with_plus7 = phone.strip().startswith('+7')
    starts_with_8 = phone.strip().startswith('8')

    required_digits = 11 if (starts_with_plus7 or starts_with_8) else 10

    if digit_count != required_digits:
        return False, 'Недопустимый ввод. Неверное количество цифр.', None

    if digit_count == 11:
        if digits[0] == '7':
            digits = '8' + digits[1:]
        formatted = f'8-{digits[1:4]}-{digits[4:7]}-{digits[7:9]}-{digits[9:11]}'
    else:
        formatted = f'8-{digits[0:3]}-{digits[3:6]}-{digits[6:8]}-{digits[8:10]}'

    return True, None, formatted


if __name__ == '__main__':
    app.run(debug=True)
