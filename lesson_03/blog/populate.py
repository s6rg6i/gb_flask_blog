from random import randint

from faker import Faker
from werkzeug.security import generate_password_hash

from blog.extension import db
from blog.models import User, Profile, Post, Category
from wsgi import app

f = Faker('ru-RU')

with app.app_context():
    users = [User(login=f'user{i}', password=generate_password_hash(f'user{i}')) for i in range(1, 11)]
    profs = [Profile(name=f.name(),
                     email=f'{users[i].login}@{f.free_email_domain()}',
                     birthday=f.date_of_birth(minimum_age=18, maximum_age=60),
                     user=users[i])
             for i in range(10)]
    cats = [Category(name=ctg) for ctg in ('В мире', 'Политика', 'Спорт', 'Культура', 'Мода', 'Юмор')]
    posts = [Post(title=f.sentence(nb_words=10),
                  content=f.sentence(nb_words=150),
                  draft=f.pybool(),
                  author=users[randint(0, len(users) - 1)],
                  category=cats[randint(0, len(cats) - 1)])
             for i in range(10)]
    db.session.add_all(users)
    db.session.add_all(profs)
    db.session.add_all(cats)
    db.session.add_all(posts)
    db.session.commit()
