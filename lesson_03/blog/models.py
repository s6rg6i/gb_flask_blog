from datetime import datetime

from flask_login import UserMixin

from blog.extension import db


class User(db.Model, UserMixin):
    """ Пользователь """
    id = db.Column(db.Integer(), primary_key=True)
    login = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(500), nullable=False)

    profile = db.relationship('Profile', back_populates='user', uselist=False, cascade="all, delete")
    post = db.relationship('Post', back_populates='author', cascade="all, delete")

    def __repr__(self):
        return f"<User id={self.id} {self.login}>"


class Profile(db.Model):
    """ Профиль пользователя (связь с User 1:1) """
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    birthday = db.Column(db.DateTime, nullable=True)
    created = db.Column(db.String(), default=datetime.utcnow)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete="CASCADE"))

    user = db.relationship('User', back_populates='profile')

    def __repr__(self):
        return f"<Profile {self.id} of user {self.user_id}>"


class Category(db.Model):
    """ Категория поста (связь с Post 1:М) """
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)

    post = db.relationship('Post', back_populates='category')

    def __repr__(self):
        return f"<Profile {self.id} of user {self.user_id}>"


class Post(db.Model):
    """ Пост (связь с User 1:М; связь с Category 1:М) """
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text(), nullable=True)
    photo = db.Column(db.String(200), nullable=True)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    updated = db.Column(db.DateTime)
    draft = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete="CASCADE"))
    category_id = db.Column(db.Integer(), db.ForeignKey('category.id', ondelete="CASCADE"))

    author = db.relationship('User', back_populates='post')
    category = db.relationship('Category', back_populates='post')

    def __repr__(self):
        return f"<Post id={self.id} {self.title}>"
