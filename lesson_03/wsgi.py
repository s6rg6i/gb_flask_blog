import click
from werkzeug.security import generate_password_hash

from blog.app import create_app
from blog.extension import db

app = create_app()


@app.cli.command('init-db')
def init_db():
    """ Команда инициализации БД """
    import blog.models
    print('Создание БД...')
    db.create_all()
    print('БД создана')


@app.cli.command('create-user')
@click.argument("name")
def create_user(name):
    """ Команда создания пользователя """
    from blog.models import User, Profile

    with app.app_context():
        db.session.add(user := User(login=name, password=generate_password_hash('user1')))
        db.session.add(prof := Profile(name='Иванов Иван'))
        prof.user = user  # user_id = user.id
        db.session.commit()

