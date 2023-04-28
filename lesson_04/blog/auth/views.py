import flask
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import logout_user, login_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash

from blog.extension import db
from blog.models import User, Profile

auth = Blueprint('auth', __name__, static_folder='../static')


@auth.route('/check-in', methods=('GET', 'POST'))
def check_in():
    if request.method == "GET":
        return render_template('auth/check-in.html')

    login = request.form.get('login')
    password = request.form.get('password')

    user = User.query.filter_by(login=login).first()
    if user and check_password_hash(user.password, password):
        login_user(user)
        return redirect(url_for('post.post_list'))

    flash('Логин или пароль введены неправильно!')
    return redirect(url_for('auth.check_in'))


@auth.route('/sign-up', methods=('GET', 'POST'))
def sign_up():
    if request.method == "GET":
        return render_template('auth/sign-up.html')

    login = request.form.get('login')
    name = request.form.get('name')
    email = request.form.get('email')
    password: str = request.form.get('password')
    confirm: str = request.form.get('confirm')
    user = User.query.filter_by(login=login).first()

    s = 'Пользователь с таким логином уже существует' if user \
        else 'Пароли не совпадают' if password != confirm else ''
    if s:
        flash(s)
        return redirect(url_for('auth.sign_up'))

    new_user = User(login=login, password=generate_password_hash(password))
    profile = Profile(name=name, email=email, user=new_user)
    db.session.add(new_user)
    db.session.add(profile)
    db.session.commit()
    user = User.query.filter_by(login=login).first()
    login_user(user)
    return redirect(url_for('post.post_list'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('post.post_list'))
