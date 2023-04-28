import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())  # загрузка пары ключ-значение из файла ".env" для установки переменных окружения

FLASK_DEBUG = os.getenv('DEBUG')
SECRET_KEY = os.getenv('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

if __name__ == "__main__":
    print(f'{FLASK_DEBUG=}')
    print(f'{SECRET_KEY=}')
    print(f'{SQLALCHEMY_DATABASE_URI=}')
    print(f'{SQLALCHEMY_TRACK_MODIFICATIONS=}')
