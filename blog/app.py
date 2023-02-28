from flask import Flask

from blog.user.views import user
from blog.article.views import article
from blog.auth.views import auth, login_manager
from blog.models.database import db


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "abcdefg123456"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)

    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(article)
    app.register_blueprint(auth)
