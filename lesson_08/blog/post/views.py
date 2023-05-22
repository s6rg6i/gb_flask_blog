import os

from flask import Blueprint, render_template, request, redirect, url_for, current_app
from flask_login import login_required, current_user

from blog.extension import db
from blog.forms.post_forms import CreatePostForm, CommentForm
from blog.functions import render_with_common_dict, get_file_name
from blog.models import User, Profile, Post, Category, Tag, Like

post = Blueprint("post", __name__, static_folder="../static")


@post.route("/", methods=('GET',))
@post.route('/index', methods=('GET',))
def post_list():
    return render_with_common_dict("post/posts.html", posts=Post.query.all())


@post.route("/<int:pk>", methods=('GET',))
def post_detail(pk: int):
    form = CommentForm()
    if request.args.get('like', ''):
        if current_user.is_authenticated:
            # проверка user, post -> 1 like
            if not Like.query.filter_by(post_id=pk, user_id=current_user.id).all():
                like = Like(post_id=pk, user_id=current_user.id)
                db.session.add(like)
                db.session.commit()
    return render_with_common_dict("post/post_detail.html", post=Post.query.get(pk), form=form)


@post.route("/tag/<int:pk>", methods=('GET',))
def posts_by_tag(pk: int):
    return render_with_common_dict("post/posts.html", posts=Tag.query.get(pk).posts)


@post.route("/ctg/<int:pk>", methods=('GET',))
def posts_by_category(pk: int):
    return render_with_common_dict("post/posts.html", posts=Category.query.get(pk).posts)


@post.route("/create", methods=('GET', 'POST'))
@login_required
def create_post():
    form = CreatePostForm(request.form)
    if request.method == "GET":
        return render_with_common_dict("post/create_post.html", form=form)
    if form.validate_on_submit():
        title = form.title.data.strip()
        content = form.content.data
        category = Category.query.get(int(form.category.data))
        file_name = None
        if f := form.photo.data:
            f.save(os.path.join(current_app.config['UPLOAD_FOLDER'], get_file_name(f.filename)))
        author = User.query.get(current_user.id)
        tags = [tag for tag in Tag.query.filter(Tag.id.in_(form.tags.data))]
        cur_post = Post(title=title, image=file_name, content=content, category=category, author=author, tags=tags)
        db.session.add(cur_post)
        db.session.commit()
        return redirect(url_for('post.post_list'))
    return render_with_common_dict("post/create_post.html", form=form)
