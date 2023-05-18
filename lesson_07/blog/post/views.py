import os
from secrets import token_hex

from flask import Blueprint, render_template, request, redirect, url_for, current_app
from flask_login import login_required, current_user
from PIL import Image
from werkzeug.exceptions import NotFound
from werkzeug.utils import secure_filename

from blog.extension import db
from blog.forms.post_forms import CreatePostForm
from blog.functions import render_with_common_dict
from blog.models import User, Profile, Post, Category, Tag

post = Blueprint("post", __name__, static_folder="../static")


@post.route("/", methods=('GET',))
@post.route('/index', methods=('GET',))
def post_list():
    return render_with_common_dict("post/posts.html", posts=Post.query.all())


@post.route("/<int:pk>", methods=('GET',))
def post_detail(pk: int):
    return render_with_common_dict("post/post_detail.html", post=Post.query.get(pk))


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
        if img_file := form.photo.data:
            f_name, f_ext = os.path.splitext(secure_filename(img_file.filename))
            file_name = f"{f_name}_{token_hex(8)}{f_ext}"
            img_file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], file_name))
        author = User.query.get(current_user.id)
        tags = [tag for tag in Tag.query.filter(Tag.id.in_(form.tags.data))]
        cur_post = Post(title=title, image=file_name, content=content, category=category, author=author, tags=tags)
        db.session.add(cur_post)
        db.session.commit()
        return redirect(url_for('post.post_list'))
    return render_with_common_dict("post/create_post.html", form=form)
