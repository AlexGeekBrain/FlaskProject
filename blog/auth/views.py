from flask import Blueprint, render_template, request, redirect, url_for, current_app
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound

from blog.models import User
from blog.models.database import db
from blog.forms.user import RegistrationForm, LoginForm


auth = Blueprint('auth', __name__, static_folder='../static')

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


@login_manager.user_loader
def load_user(pk):
    return User.query.filter_by(id=pk).one_or_none()


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('auth.login'))


__all__ = [
    'login_manager',
    'auth',
]



@auth.route('/register/', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect('index.get_index')

    error = None
    form = RegistrationForm(request.form)
    if request.method == "POST" and form.validate_on_submit():
        if User.query.filter_by(username=form.username.data).count():
            form.username.errors.append('username already exists!')
            return render_template('auth/register.html', form=form)

        if User.query.filter_by(email=form.email.data).count():
            form.email.errors.append('email already exists!')
            return render_template('auth/register.html', form=form)

        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            username=form.username.data,
            email=form.email.data,
            is_staff=False,
        )
        user.password = form.password.data
        db.session.add(user)
        try:
            db.session.commit()
        except IntegrityError:
            current_app.logger.exception('Could not create user!')
            error = 'Could not create user!'
        else:
            current_app.logger.info('Created user %s', user)
            login_user(user)
            return redirect(url_for('index.get_index'))
    return render_template('auth/register.html', form=form, error=error)


@auth.route('/login/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('index.get_index')
    
    form = LoginForm(request.form)
    
    if request.method == "POST" and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).one_or_none()
        if user is None:
            return render_template('auth/login.html', form=form, error="username doesn't exist")
        if not user.validate_password(form.password.data):
            return render_template('auth/login.html', form=form, error='invalid username or password')
        
        login_user(user)
        return redirect(url_for('index.get_index'))
    return render_template('auth/login.html', form=form)
        
    
@auth.route('/login-as/', methods=['GET', 'POST'])
def login_as():
    if not (current_user.is_authenticated and current_user.is_staff):
        raise NotFound
    
    if request.method == 'GET':
        return render_template('auth/login.html')
    
    username = request.form.get('username')
    if not username:
        return render_template('auth/login.html', error='username not passed')
    
    user = User.query.filter_by(username=username).one_or_none()
    if user is None:
        return render_template('auth/login.html', error=f'no user {username} found')
    
    login_user(user)
    return redirect(url_for('index.get_index'))


@auth.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index.get_index'))


@auth.route('/secret/')
@login_required
def secret_view():
    return 'Super secret data'
