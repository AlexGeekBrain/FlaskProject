from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

from blog.models import User


users = Blueprint('users', __name__, url_prefix='/users', static_folder='../static')


@users.route('/')
def user_list():
    users = User.query.all()
    return render_template(
        'users/list.html',
        users=users,
        )


@users.route('/<int:pk>')
def user_details(pk: int):
    user = User.query.filter_by(id=pk).one_or_none()
    if user is None:
        raise NotFound(f'Пользователь #{pk} не найден!')
    return render_template(
        'users/details.html',
        user=user,
        )
