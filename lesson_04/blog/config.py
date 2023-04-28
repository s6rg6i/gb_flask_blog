import os

from dotenv import load_dotenv, find_dotenv
from flask import Config

load_dotenv(find_dotenv())  # загрузка пары ключ-значение из файла ".env" для установки переменных окружения


class BaseConfig:
    FLASK_DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SECRET_KEY = os.getenv('SECRET_KEY')


class DevConfig(BaseConfig):
    FLASK_DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'


class TestConfig(BaseConfig):
    TESTING = True


if __name__ == "__main__":
    # cfg_name = 'BaseConfig'
    # cfg_name = 'DevConfig'
    cfg_name = 'TestConfig'

    Config("").from_object(f'config.{cfg_name}')
    print('FLASK_DEBUG=', eval(f'{cfg_name}.FLASK_DEBUG'))
    print('TESTING=', eval(f'{cfg_name}.TESTING'))
    print('SQLALCHEMY_TRACK_MODIFICATIONS=', eval(f'{cfg_name}.SQLALCHEMY_TRACK_MODIFICATIONS'))
    print('SQLALCHEMY_DATABASE_URI=', eval(f'{cfg_name}.SQLALCHEMY_DATABASE_URI'))
    print('SECRET_KEY=', eval(f'{cfg_name}.SECRET_KEY'))

