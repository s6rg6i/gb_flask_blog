### 3. Авторизация пользователя и начало работы с базой данных. SQLAlchemy.

---

#### Практическое задание:

* Подключить Flask-SQLAlchemy в свой Flask проект.
* Создать базовую модель пользователя, добавить к ней UserMixin.
* Добавить страницу авторизации.
* Создать один view, который недоступен анонимным пользователям.

#### Установлены зависимости:

* Flask-SQLAlchemy 3.0.3 - [https://pypi.org/project/Flask-SQLAlchemy/]
* Flask-Login 0.6.2 - [https://pypi.org/project/Flask-Login/]
* python-dotenv 1.0.0 - [https://pypi.org/project/python-dotenv//]

#### Выполнено

* Создан файл конфигурации проекта
  * Создан файл - _.env_
  * Создан файл - _config.py_, считывающий переменные окружения из _.env_
* Подключен Flask-SQLAlchemy в проект "blog"
  * В файле _extension.py_: `db = SQLAlchemy()  app.py: db.init_app(app)`
  * В файле _app.py_: `db.init_app(app)`
* Созданы модели
  * В файле _models.py_ `User, Profile, Category, Post`
* Созданы пользовательские команды
  * Команда инициализации БД `init-db`
  * Команда создания пользователя `create-user`
* Создан файл _populate.py_. Запуск этого модуля заполняет тестовыми данными таблицы БД.
* Изменены контроллеры и шаблоны для работы с БД
* Добавлена аутентификация в приложение с помощью пакета Flask-Login
  * Добавлен blueprint `auth`
  * Добавлен mixin в модель **User**: `class User(db.Model, UserMixin)`
  * Создан LoginManager класс `login_manager = LoginManager()`
  * В blueprint **auth** добавлены **views**: `check_in, sign_up, logout`
  * В _templates/auth_ добавлен: `check_in.html, sign_up.html`
