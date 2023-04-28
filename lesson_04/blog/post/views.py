from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

from blog.models import User, Profile, Post, Category

post = Blueprint("post", __name__, static_folder="../static")


@post.route("/")
def post_list():
    return render_template("post/posts.html", posts=Post.query.all())


@post.route("/<int:pk>")
def post_detail(pk: int):
    return render_template("post/post_detail.html", post=Post.query.get(pk))

