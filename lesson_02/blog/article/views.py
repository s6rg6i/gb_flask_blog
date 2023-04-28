
from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

from blog.data import articles, get_users_by_id, get_article_by_id, get_user_by_id

article = Blueprint("article", __name__, url_prefix="", static_folder="../static")


@article.route("/")
def article_list():
    return render_template("article/articles.html", articles=articles, users_by_id=get_users_by_id())


@article.route("/<int:pk>")
def article_detail(pk: int):
    art = get_article_by_id(pk)
    user = get_user_by_id(art.get('author_id'))
    if art and user:
        return render_template("article/article_detail.html", article=art, user=user)
    raise NotFound(f"Не существует автора с id:{art.get('author_id')} или статьи с id:{pk}!")
