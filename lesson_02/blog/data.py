from dataclasses import dataclass, asdict
from random import randint

from faker import Faker


@dataclass
class User:
    id: int
    login: str
    name: str


@dataclass
class Article:
    id: int
    title: str
    content: str
    author_id: int


f = Faker('ru-RU')
users = [User(id=i, login=f.user_name(), name=f.name()) for i in range(1, 11)]
articles = [Article(id=i, title=f.sentence(nb_words=10), content=f.sentence(nb_words=150),
                    author_id=randint(1, len(users))) for i in range(1, 15)]


def get_users_by_id() -> dict:
    """ Получить словарь пользователей {id: {'id':..., 'login':...} ...} """
    return {user.id: asdict(user) for user in users}


def get_user_by_id(pk: int) -> dict:
    """ Получить пользователя по id """
    return get_users_by_id().get(pk, None)


def get_articles_by_id() -> dict:
    """ Получить словарь статей {id: {id: {'id':..., 'title':...} ...} """
    return {article.id: asdict(article) for article in articles}


def get_article_by_id(pk: int) -> dict:
    """ Получить статью по id """
    return get_articles_by_id().get(pk, None)


if __name__ == '__main__':
    for art in articles:
        print(art.id)
        print(art.title)
        print(art.content)
    print(get_article_by_id(1))
    print(get_user_by_id(1))


