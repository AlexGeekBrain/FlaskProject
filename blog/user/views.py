from flask import Blueprint, render_template, redirect
from werkzeug.exceptions import NotFound


user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')

USERS = {
    1: 'Alex',
    2: 'Oleg',
    3: 'Nina',
}


@user.route('/')
def user_list():
    return render_template(
        'users/list.html',
        users=USERS,
        )


@user.route('/<int:pk>')
def get_user(pk: int):
    try:
        user_name = USERS[pk]
    except KeyError:
        raise NotFound(f'User id {pk} not found')
        # return redirect('/users/')
    return render_template(
        'users/details.html',
        user_name=user_name,
        )
