from datetime import datetime

from flask_login import UserMixin

from blog.extension import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    """ Пользователь """
    id = db.Column(db.Integer(), primary_key=True)
    login = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(500), nullable=False)
    is_staff = db.Column(db.Boolean, default=False)

    profile = db.relationship('Profile', back_populates='user', uselist=False, cascade="all, delete")
    post = db.relationship('Post', back_populates='author', cascade="all, delete")

    def __repr__(self):
        return f"<User id={self.id} {self.login}>"


class Profile(db.Model):
    """ Профиль пользователя (связь с User 1:1) """
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), unique=True)
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

    posts = db.relationship('Post', back_populates='category')

    def __repr__(self):
        return f"<{self.name}>"


post_tag = db.Table('post_tag', db.metadata,
                    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
                    db.Column('post_id', db.Integer, db.ForeignKey('post.id')))


class Post(db.Model):
    """ Post: связь с User 1:M; связь с Category 1:М; связь с Tag M:М) """
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String(200), nullable=True)
    content = db.Column(db.Text(), nullable=True)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    updated = db.Column(db.DateTime)
    draft = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete="CASCADE"))
    category_id = db.Column(db.Integer(), db.ForeignKey('category.id', ondelete="CASCADE"))

    author = db.relationship('User', back_populates='post')
    category = db.relationship('Category', back_populates='posts')
    likes = db.relationship('Like', back_populates='posts')

    tags = db.relationship('Tag', secondary=post_tag, back_populates='posts')

    def __repr__(self):
        return f"<Post id={self.id} {self.title}>"


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    posts = db.relationship('Post', secondary=post_tag, back_populates='tags')

    def __repr__(self):
        return f"<Tag {self.title}>"


class Like(db.Model):
    """ Лайки под постом (связь с Post 1:М и User 1:M) """
    id = db.Column(db.Integer(), primary_key=True)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete="CASCADE"))
    post_id = db.Column(db.Integer(), db.ForeignKey('post.id', ondelete="CASCADE"))

    posts = db.relationship('Post', back_populates='likes')

    def __repr__(self):
        return f"<user:{self.user_id}, post:{self.post_id}>"
