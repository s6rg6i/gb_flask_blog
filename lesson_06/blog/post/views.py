from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from werkzeug.exceptions import NotFound

from blog.extension import db
from blog.forms.post_forms import CreatePostForm
from blog.models import User, Profile, Post, Category

post = Blueprint("post", __name__, static_folder="../static")


@post.route("/", methods=('GET',))
def post_list():
    return render_template("post/posts.html", posts=Post.query.all())


@post.route("/<int:pk>", methods=('GET',))
def post_detail(pk: int):
    return render_template("post/post_detail.html", post=Post.query.get(pk))


@post.route("/create", methods=('GET', 'POST'))
@login_required
def create_post():
    form = CreatePostForm(request.form)
    if request.method == "GET":
        return render_template("post/create_post.html", form=form)
    if form.validate_on_submit():
        title = form.title.data.strip()
        content = form.content.data
        category = Category.query.get(int(form.category.data))
        author = User.query.get(current_user.id)
        cur_post = Post(title=title, content=content, category=category, author=author)

        db.session.add(cur_post)
        db.session.commit()
        return redirect(url_for('post.post_list'))
    return render_template("post/create_post.html", form=form)
