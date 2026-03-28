from flask import Blueprint, render_template, request, make_response
from flask_login import current_user
from models import db, VisitLog, User
from auth import check_rights
from sqlalchemy import func
import csv
from io import StringIO

visit_logs_bp = Blueprint('visit_logs', __name__, url_prefix='/logs')

# Главная страница журнала посещений
@visit_logs_bp.route('/')
@check_rights('view_logs')
def index():
    page = request.args.get('page', 1, type=int)
    per_page = 20

    # Для обычных пользователей показываем только их записи
    query = VisitLog.query
    if not current_user.is_admin():
        query = query.filter_by(user_id=current_user.id)

    # Сортировка по убыванию даты
    pagination = query.order_by(VisitLog.created_at.desc()).paginate(
        page=page,
        per_page=per_page,
        error_out=False
    )

    return render_template('visit_logs/index.html',
                           logs=pagination.items,
                           pagination=pagination,
                           title='Журнал посещений')


# Отчёт по страницам
@visit_logs_bp.route('/stats/pages')
@check_rights('view_stats')
def stats_pages():
    # Группировка по страницам с подсчётом количества
    stats = db.session.query(
        VisitLog.path,
        func.count(VisitLog.id).label('count')
    ).group_by(VisitLog.path).order_by(func.count(VisitLog.id).desc()).all()

    return render_template('visit_logs/stats_pages.html',
                           stats=stats,
                           title='Отчёт по страницам')


# Экспорт отчёта по страницам в CSV
@visit_logs_bp.route('/stats/pages/export')
@check_rights('view_stats')
def export_pages():
    # Получение данных
    stats = db.session.query(
        VisitLog.path,
        func.count(VisitLog.id).label('count')
    ).group_by(VisitLog.path).order_by(func.count(VisitLog.id).desc()).all()

    # Создание CSV
    si = StringIO()
    writer = csv.writer(si, delimiter=';')
    writer.writerow(['№', 'Страница', 'Количество посещений'])

    for i, (path, count) in enumerate(stats, 1):
        writer.writerow([i, path, count])

    # Создание ответа с BOM для корректного отображения кириллицы в Excel
    output = make_response('\ufeff' + si.getvalue())
    output.headers['Content-Disposition'] = 'attachment; filename=pages_stats.csv'
    output.headers['Content-type'] = 'text/csv; charset=utf-8'

    return output


# Отчёт по пользователям
@visit_logs_bp.route('/stats/users')
@check_rights('view_stats')
def stats_users():
    # Группировка по пользователям
    stats = db.session.query(
        VisitLog.user_id,
        func.count(VisitLog.id).label('count')
    ).group_by(VisitLog.user_id).order_by(func.count(VisitLog.id).desc()).all()

    # Получение информации о пользователях
    user_stats = []
    for user_id, count in stats:
        if user_id:
            user = User.query.get(user_id)
            user_name = user.get_full_name() if user else 'Неизвестный пользователь'
        else:
            user_name = 'Неаутентифицированный пользователь'

        user_stats.append({
            'user_id': user_id,
            'user_name': user_name,
            'count': count
        })

    return render_template('visit_logs/stats_users.html',
                           stats=user_stats,
                           title='Отчёт по пользователям')


# Экспорт отчёта по пользователям в CSV
@visit_logs_bp.route('/stats/users/export')
@check_rights('view_stats')
def export_users():
    # Получение данных
    stats = db.session.query(
        VisitLog.user_id,
        func.count(VisitLog.id).label('count')
    ).group_by(VisitLog.user_id).order_by(func.count(VisitLog.id).desc()).all()

    # Создание CSV
    si = StringIO()
    writer = csv.writer(si, delimiter=';')
    writer.writerow(['№', 'Пользователь', 'Количество посещений'])

    for i, (user_id, count) in enumerate(stats, 1):
        if user_id:
            user = User.query.get(user_id)
            user_name = user.get_full_name() if user else 'Неизвестный пользователь'
        else:
            user_name = 'Неаутентифицированный пользователь'

        writer.writerow([i, user_name, count])

    # Создание ответа с BOM для корректного отображения кириллицы в Excel
    output = make_response('\ufeff' + si.getvalue())
    output.headers['Content-Disposition'] = 'attachment; filename=users_stats.csv'
    output.headers['Content-type'] = 'text/csv; charset=utf-8'

    return output
