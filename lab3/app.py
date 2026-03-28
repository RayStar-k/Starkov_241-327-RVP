from flask import Flask, render_template, session, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here-change-in-production'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Для доступа к этой странице необходимо пройти процедуру аутентификации.'
login_manager.login_message_category = 'warning'

class User(UserMixin):
    def __init__(self, id):
        self.id = id
        self.password_hash = generate_password_hash('qwerty')

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

users = {'user': User('user')}

@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)

@app.route('/')
def index():
    return render_template('index.html', title='Главная')

@app.route('/counter')
def counter():
    if 'visit_count' in session:
        session['visit_count'] += 1
    else:
        session['visit_count'] = 1

    visit_count = session['visit_count']
    return render_template('counter.html', title='Счётчик посещений', visit_count=visit_count)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        remember = request.form.get('remember')

        user = users.get(username)
        if user and user.check_password(password):
            login_user(user, remember=bool(remember))

            next_page = request.args.get('next')

            if next_page and next_page.startswith('/'):
                return redirect(next_page)

            flash('Вы успешно вошли в систему!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Неверно введён логин или пароль. Попробуйте снова.', 'danger')

    return render_template('login.html', title='Вход')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Вы вышли из системы.', 'info')
    return redirect(url_for('index'))

@app.route('/secret')
@login_required
def secret():
    return render_template('secret.html', title='Секретная страница')

if __name__ == '__main__':
    app.run(debug=True)
