from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from config import Config
from models import db, User, Role
from validators import validate_user_form, validate_password
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config.from_object(Config)


db.init_app(app)

# Настройка Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Для доступа к этой странице необходимо пройти процедуру аутентификации.'
login_manager.login_message_category = 'warning'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Главная страница - список пользователей
@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users, title='Список пользователей')

# Просмотр пользователя
@app.route('/users/<int:user_id>')
def view_user(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('view_user.html', user=user, title=f'Просмотр пользователя')

# Создание пользователя
@app.route('/users/create', methods=['GET', 'POST'])
@login_required
def create_user():
    roles = Role.query.all()

    if request.method == 'POST':
        form_data = {
            'login': request.form.get('login', '').strip(),
            'password': request.form.get('password', ''),
            'last_name': request.form.get('last_name', '').strip(),
            'first_name': request.form.get('first_name', '').strip(),
            'middle_name': request.form.get('middle_name', '').strip(),
            'role_id': request.form.get('role_id', '')
        }

        # Валидация
        errors = validate_user_form(form_data, is_edit=False, require_password=True)

        if errors:
            return render_template('user_form.html',
                                   form_data=form_data,
                                   errors=errors,
                                   roles=roles,
                                   is_edit=False,
                                   title='Создание пользователя')

        # Создание пользователя
        try:
            user = User(
                login=form_data['login'],
                last_name=form_data['last_name'] if form_data['last_name'] else None,
                first_name=form_data['first_name'],
                middle_name=form_data['middle_name'] if form_data['middle_name'] else None,
                role_id=int(form_data['role_id']) if form_data['role_id'] else None
            )
            user.set_password(form_data['password'])

            db.session.add(user)
            db.session.commit()

            flash('Пользователь успешно создан!', 'success')
            return redirect(url_for('index'))

        except IntegrityError:
            db.session.rollback()
            flash('Ошибка: пользователь с таким логином уже существует.', 'danger')
            return render_template('user_form.html',
                                   form_data=form_data,
                                   errors=errors,
                                   roles=roles,
                                   is_edit=False,
                                   title='Создание пользователя')
        except Exception as e:
            db.session.rollback()
            flash(f'Произошла ошибка при создании пользователя: {str(e)}', 'danger')
            return render_template('user_form.html',
                                   form_data=form_data,
                                   errors=errors,
                                   roles=roles,
                                   is_edit=False,
                                   title='Создание пользователя')

    return render_template('user_form.html',
                           form_data={},
                           errors={},
                           roles=roles,
                           is_edit=False,
                           title='Создание пользователя')

# Редактирование пользователя
@app.route('/users/<int:user_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    roles = Role.query.all()

    if request.method == 'POST':
        form_data = {
            'last_name': request.form.get('last_name', '').strip(),
            'first_name': request.form.get('first_name', '').strip(),
            'middle_name': request.form.get('middle_name', '').strip(),
            'role_id': request.form.get('role_id', '')
        }

        # Валидация
        errors = validate_user_form(form_data, is_edit=True, require_password=False)

        if errors:
            return render_template('user_form.html',
                                   form_data=form_data,
                                   errors=errors,
                                   roles=roles,
                                   is_edit=True,
                                   user=user,
                                   title='Редактирование пользователя')

        # Обновление пользователя
        try:
            user.last_name = form_data['last_name'] if form_data['last_name'] else None
            user.first_name = form_data['first_name']
            user.middle_name = form_data['middle_name'] if form_data['middle_name'] else None
            user.role_id = int(form_data['role_id']) if form_data['role_id'] else None

            db.session.commit()

            flash('Данные пользователя успешно обновлены!', 'success')
            return redirect(url_for('index'))

        except Exception as e:
            db.session.rollback()
            flash(f'Произошла ошибка при обновлении данных: {str(e)}', 'danger')
            return render_template('user_form.html',
                                   form_data=form_data,
                                   errors=errors,
                                   roles=roles,
                                   is_edit=True,
                                   user=user,
                                   title='Редактирование пользователя')

    # GET запрос - отображаем форму с текущими данными
    form_data = {
        'last_name': user.last_name or '',
        'first_name': user.first_name or '',
        'middle_name': user.middle_name or '',
        'role_id': str(user.role_id) if user.role_id else ''
    }

    return render_template('user_form.html',
                           form_data=form_data,
                           errors={},
                           roles=roles,
                           is_edit=True,
                           user=user,
                           title='Редактирование пользователя')

# Удаление пользователя
@app.route('/users/<int:user_id>/delete', methods=['POST'])
@login_required
def delete_user(user_id):
    user = User.query.get_or_404(user_id)

    try:
        db.session.delete(user)
        db.session.commit()
        flash('Пользователь успешно удалён!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Произошла ошибка при удалении пользователя: {str(e)}', 'danger')

    return redirect(url_for('index'))

# Вход в систему
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method == 'POST':
        login_name = request.form.get('login')
        password = request.form.get('password')
        remember = request.form.get('remember')

        user = User.query.filter_by(login=login_name).first()

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

# Выход из системы
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Вы вышли из системы.', 'info')
    return redirect(url_for('index'))

# Изменение пароля
@app.route('/change-password', methods=['GET', 'POST'])
@login_required
def change_password():
    if request.method == 'POST':
        old_password = request.form.get('old_password', '')
        new_password = request.form.get('new_password', '')
        confirm_password = request.form.get('confirm_password', '')

        errors = {}

        # Проверка старого пароля
        if not current_user.check_password(old_password):
            errors['old_password'] = ['Неверный пароль']

        # Валидация нового пароля
        new_password_errors = validate_password(new_password)
        if new_password_errors:
            errors['new_password'] = new_password_errors

        # Проверка совпадения паролей
        if new_password != confirm_password:
            errors['confirm_password'] = ['Пароли не совпадают']

        if errors:
            return render_template('change_password.html',
                                   errors=errors,
                                   title='Изменение пароля')

        # Обновление пароля
        try:
            current_user.set_password(new_password)
            db.session.commit()
            flash('Пароль успешно изменён!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash(f'Произошла ошибка при изменении пароля: {str(e)}', 'danger')

    return render_template('change_password.html', errors={}, title='Изменение пароля')

if __name__ == '__main__':
    app.run(debug=True)
