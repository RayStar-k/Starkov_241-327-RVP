from functools import wraps
from flask import flash, redirect, url_for
from flask_login import current_user


def check_rights(action):
    """
    Декоратор для проверки прав пользователя на выполнение действий.

    Права доступа:
    - Администратор: все действия
    - Пользователь: только редактирование своих данных и просмотр своего профиля

    Параметры:
    - action: тип действия ('create_user', 'edit_user', 'view_user', 'delete_user', 'view_logs')
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # Проверка аутентификации
            if not current_user.is_authenticated:
                flash('Для доступа к этой странице необходимо пройти процедуру аутентификации.', 'warning')
                return redirect(url_for('login'))

            # Администратор имеет доступ ко всем действиям
            if current_user.is_admin():
                return f(*args, **kwargs)

            # Проверка прав для обычных пользователей
            if action == 'create_user':
                flash('У вас недостаточно прав для доступа к данной странице.', 'danger')
                return redirect(url_for('index'))

            elif action == 'delete_user':
                flash('У вас недостаточно прав для доступа к данной странице.', 'danger')
                return redirect(url_for('index'))

            elif action == 'edit_user':
                # Пользователь может редактировать только свои данные
                user_id = kwargs.get('user_id')
                if user_id != current_user.id:
                    flash('У вас недостаточно прав для доступа к данной странице.', 'danger')
                    return redirect(url_for('index'))
                return f(*args, **kwargs)

            elif action == 'view_user':
                # Пользователь может просматривать только свой профиль
                user_id = kwargs.get('user_id')
                if user_id != current_user.id:
                    flash('У вас недостаточно прав для доступа к данной странице.', 'danger')
                    return redirect(url_for('index'))
                return f(*args, **kwargs)

            elif action == 'view_logs':
                # Пользователь может просматривать журнал посещений
                return f(*args, **kwargs)

            elif action == 'view_stats':
                # Только администратор может просматривать статистику
                flash('У вас недостаточно прав для доступа к данной странице.', 'danger')
                return redirect(url_for('index'))

            # По умолчанию запрещаем доступ
            flash('У вас недостаточно прав для доступа к данной странице.', 'danger')
            return redirect(url_for('index'))

        return decorated_function
    return decorator
