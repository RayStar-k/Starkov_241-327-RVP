import re

def validate_login(login):
    """
    Проверяет логин на соответствие требованиям:
    - только латинские буквы и цифры
    - минимум 5 символов
    """
    errors = []

    if not login:
        errors.append("Поле не может быть пустым")
        return errors

    if len(login) < 5:
        errors.append("Логин должен содержать не менее 5 символов")

    if not re.match(r'^[a-zA-Z0-9]+$', login):
        errors.append("Логин должен состоять только из латинских букв и цифр")

    return errors

def validate_password(password):
    """
    Проверяет пароль на соответствие требованиям:
    - не менее 8 символов
    - не более 128 символов
    - как минимум одна заглавная и одна строчная буква
    - только латинские или кириллические буквы
    - как минимум одна цифра
    - только арабские цифры
    - без пробелов
    - Другие допустимые символы: ~ ! ? @ # $ % ^ & * _ - + ( ) [ ] { } > < / \\ | " ' . , : ;
    """
    errors = []

    if not password:
        errors.append("Поле не может быть пустым")
        return errors

    if len(password) < 8:
        errors.append("Пароль должен содержать не менее 8 символов")

    if len(password) > 128:
        errors.append("Пароль должен содержать не более 128 символов")

    # Проверка на наличие заглавных и строчных букв
    if not re.search(r'[A-ZА-ЯЁ]', password):
        errors.append("Пароль должен содержать хотя бы одну заглавную букву")

    if not re.search(r'[a-zа-яё]', password):
        errors.append("Пароль должен содержать хотя бы одну строчную букву")

    # Проверка на наличие цифр
    if not re.search(r'[0-9]', password):
        errors.append("Пароль должен содержать хотя бы одну цифру")

    # Проверка на пробелы
    if ' ' in password:
        errors.append("Пароль не должен содержать пробелы")

    # Проверка допустимых символов
    # Допустимы: латинские/кириллические буквы, цифры и специальные символы
    allowed_special = r'~!?@#$%^&*_\-+()[\]{}<>/\\|"\'.,:;'
    pattern = f'^[a-zA-Zа-яА-ЯёЁ0-9{re.escape(allowed_special)}]+$'

    if not re.match(pattern, password):
        errors.append("Пароль содержит недопустимые символы")

    # Проверка, что буквы только латинские ИЛИ только кириллические (не вместе)
    has_latin = bool(re.search(r'[a-zA-Z]', password))
    has_cyrillic = bool(re.search(r'[а-яА-ЯёЁ]', password))

    if has_latin and has_cyrillic:
        errors.append("Пароль должен содержать только латинские или только кириллические буквы")

    return errors

def validate_name(name, field_name="Поле"):
    """
    Проверяет, что поле не пустое
    """
    errors = []

    if not name or not name.strip():
        errors.append(f"{field_name} не может быть пустым")

    return errors

def validate_user_form(form_data, is_edit=False, require_password=True):
    """
    Валидация формы пользователя

    Args:
        form_data: словарь с данными формы
        is_edit: True если это редактирование (не проверяем логин и пароль)
        require_password: True если пароль обязателен

    Returns:
        dict: словарь с ошибками для каждого поля
    """
    errors = {}

    # Проверка логина (только при создании)
    if not is_edit:
        login_errors = validate_login(form_data.get('login', ''))
        if login_errors:
            errors['login'] = login_errors

    # Проверка пароля (только при создании или если require_password=True)
    if not is_edit and require_password:
        password_errors = validate_password(form_data.get('password', ''))
        if password_errors:
            errors['password'] = password_errors

    # Проверка имени (обязательное поле)
    first_name_errors = validate_name(form_data.get('first_name', ''), "Имя")
    if first_name_errors:
        errors['first_name'] = first_name_errors

    # Фамилия и отчество необязательны, но если заполнены, проверяем
    # Роль также необязательна

    return errors
