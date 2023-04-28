### 4. Docker, docker-compose, Postgres. Миграции схем Flask-Migrate и alembic.

---

#### Практическое задание:

* Собрать докер-образ со своим проектом.
* Подключить Postgres к своему Flask проекту.
* Обновить модель пользователя.
* Сгенерировать автоматическую миграцию на создание схемы пользователя.
* Добавить миграцию данных для создания стандартного админа.

#### Установлены зависимости:

* Flask-Migrate 4.0.4 - [https://pypi.org/project/Flask-Migrate/]
* psycopg2-binary 2.9.6 - [https://pypi.org/project/psycopg2-binary/]

#### Выполнено

* Применен объектно-ориентированный подход к управлению конфигурациями
  * Секретные значения в _.env_
  * В файле _config.py_ классы для различных конфигураций
  * Загрузка переменных в _app.py_:
* Doker
  * Установлен **Docker Toolbox** for Windows 10 (устаревший, но менее ресурсоемкий, чем **Docker Desktop**
  * Создан _Dockerfile_ и _docker-compose.yaml_ файл.
    Созданы образы приложения **Blog** и базы данных **Postgres** и запущены контейнеры.
* Миграции
  + В файле _extension.py_ создали: `migrate = Migrate()`
  + В файле _app.py_ зарегистрировали `migrate.init_app(app, db)`
  + Выполняем инициализацию в терминале `flask db init`
  + Добавили в модель **User** поле `is_staff = db.Column(db.Boolean, default=False)`
  + Запустили в терминале миграции `flask db migrate -m 'changed User  model'`
  + Провели миграцию `flask db upgrade`