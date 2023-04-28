import os

from flask import Flask

from blog.extension import db, login_manager, migrate
from blog.auth.views import auth
from blog.models import User
from blog.post.views import post
from blog.user.views import user
from blog.config import *


def create_app() -> Flask:
    app = Flask(__name__)
    cfg_name = os.getenv("CONFIG_NAME") or "BaseConfig"
    app.config.from_object(f"blog.config.{cfg_name}")
    # app.config.from_object('blog.config')
    register_extensions(app)  # register db
    register_blueprints(app)  # register Blueprints
    # register_commands(app)  # register console commands
    return app


def register_extensions(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


def register_blueprints(app: Flask):
    """ Регистрация блюпринтов """
    [app.register_blueprint(bp) for bp in (user, post, auth)]
