import flask
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import logout_user, login_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash

from blog.extension import db
from blog.forms.user_forms import UserRegisterForm, UserLoginForm
from blog.models import User, Profile

auth = Blueprint('auth', __name__, static_folder='../static')


@auth.route('/login', methods=('GET', 'POST'))
def login():
    """ Форма login через WTForms """
    form = UserLoginForm(request.form)
    if request.method == 'GET':
        form.next.data = request.args.get("next", "/")
        return render_template('auth/login.html', form=form)

    login_name = form.login.data
    password = form.password.data
    _next = form.next.data

    if form.validate_on_submit():
        if not User.query.filter_by(login=login_name).count():
            form.login.errors.append('Пользователя с таким именем не существует')
            return render_template('auth/login.html', form=form)
        user = User.query.filter_by(login=login_name).first()
        if check_password_hash(user.password, password):
            form.password.errors.append('Неправильный пароль')
            return render_template('auth/login.html', form=form)

        login_user(user)
        return redirect(_next)

    return render_template('auth/login.html', form=form)


@auth.route('/register', methods=('GET', 'POST'))
def register():
    """ Форма регистрации через WTForms """
    if current_user.is_authenticated:
        return redirect(url_for('post.post_list'))

    form = UserRegisterForm(request.form)

    login_name = form.login.data
    name = form.name.data
    email = form.email.data
    password = form.password.data

    if request.method == 'POST' and form.validate_on_submit():
        err = False
        if Profile.query.filter_by(email=form.email.data).count():
            form.email.errors.append('Почтовый адрес уже существует')
            err = True
        if User.query.filter_by(login=login_name).count():
            form.login.errors.append('Пользователь с таким именем уже существует')
            err = True
        if err:
            return render_template('auth/register.html', form=form)

        new_user = User(login=login_name, password=generate_password_hash(password))
        profile = Profile(name=name, email=email, user=new_user)
        db.session.add(new_user)
        db.session.add(profile)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('post.post_list'))

    return render_template('auth/register.html', form=form)


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
    """ Форма регистрации через форму HTML """
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
