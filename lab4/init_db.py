from app import app
from models import db, User, Role

def init_database():

    with app.app_context():
        print("Удаление существующих таблиц...")
        db.drop_all()

        print("Создание таблиц...")
        db.create_all()

        print("Создание ролей...")
        roles_data = [
            {'name': 'Администратор', 'description': 'Полный доступ к системе'},
            {'name': 'Модератор', 'description': 'Управление контентом'},
            {'name': 'Пользователь', 'description': 'Базовый доступ к системе'},
        ]

        roles = {}
        for role_data in roles_data:
            role = Role(**role_data)
            db.session.add(role)
            roles[role_data['name']] = role

        db.session.commit()
        print(f"Создано ролей: {len(roles)}")

        print("Создание пользователей...")
        users_data = [
            {
                'login': 'admin',
                'password': 'Admin123',
                'last_name': 'Старков',
                'first_name': 'Руслан',
                'middle_name': 'Владимирович',
                'role': roles['Администратор']
            },
            {
                'login': 'moderator',
                'password': 'Moder123',
                'last_name': 'Усманов',
                'first_name': 'Али',
                'middle_name': 'Руждиевич',
                'role': roles['Модератор']
            },
            {
                'login': 'user1',
                'password': 'User1234',
                'last_name': 'Иванченко',
                'first_name': 'Александр',
                'middle_name': None,
                'role': roles['Пользователь']
            },
            {
                'login': 'user2',
                'password': 'Password1',
                'last_name': 'Плотникова',
                'first_name': 'Анна',
                'middle_name': 'Александровна',
                'role': None
            },
            {
                'login': 'testuser',
                'password': 'Test1234',
                'last_name': None,
                'first_name': 'Тест',
                'middle_name': 'Тестович',
                'role': roles['Пользователь']
            },
        ]

        for user_data in users_data:
            password = user_data.pop('password')
            role = user_data.pop('role')

            user = User(**user_data)
            user.set_password(password)
            user.role = role

            db.session.add(user)

        db.session.commit()
        print(f"Создано пользователей: {len(users_data)}")

        print("\nБаза данных успешно инициализирована!")
        print("\nДля входа можете использовать следующие учётные записи:")
        print("┌──────────────┬─────────────┐")
        print("│ Логин        │ Пароль      │")
        print("├──────────────┼─────────────┤")
        print("│ admin        │ Admin123    │")
        print("│ moderator    │ Moder123    │")
        print("│ user1        │ User1234    │")
        print("│ user2        │ Password1   │")
        print("│ testuser     │ Test1234    │")
        print("└──────────────┴─────────────┘")

if __name__ == '__main__':
    init_database()
