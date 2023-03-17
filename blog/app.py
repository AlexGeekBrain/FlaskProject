import os
from flask import Flask
from flask_migrate import Migrate

from blog.index.views import index
from blog.user.views import user
from blog.article.views import articles
from blog.authors.views import authors
from blog.auth.views import auth, login_manager

from blog.models.database import db
from blog.security import flask_bcrypt
from blog.admin import admin


migrate = Migrate()


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "abcdefg123456"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    cfg_name = os.environ.get('CONFIG_NAME') or 'BaseConfig'
    app.config.from_object(f'blog.configs.{cfg_name}')

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    flask_bcrypt.init_app(app)
    admin.init_app(app)

    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(index)
    app.register_blueprint(user, name='users')
    app.register_blueprint(articles)
    app.register_blueprint(auth)
    app.register_blueprint(authors)
