from flask import Flask

from blog.article.views import article
from blog.user.views import user


def create_app() -> Flask:
    app = Flask(__name__)
    [app.register_blueprint(bp) for bp in (user, article)]  # register Blueprints
    return app
