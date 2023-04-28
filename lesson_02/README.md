### Урок 2. Flask - Blueprints, функции: render_template, redirect, url_for. Jinja2

---

#### Практическое задание:

* Добавить в свой проект на Flask использование шаблонов и стилей Bootstrap.
* В базовый шаблон добавить навигационную панель, которая будет отображаться на всех страницах ресурса.
* Реализовать страницы со списком доступных статей и пользователей, а также возможность перехода к их деталям.

#### Установлены зависимости:

* Faker 18.6.0 - [https://pypi.org/project/Faker/]

#### Выполнено

* Созданы **article**, **user** blueprints.
* В файле **data.py** списки `users` и `articles` заполнены тестовыми данными
* К шаблонам подключен фреймворк **Bootstrap** и иконочный шрифт **Font Awesome**
* Созданы базовые шаблоны **base.html**, **_navbar.html**, **_right.html**
* В _blog/templates/article_ созданы шаблоны **articles.html**, **article_detail.html**
* В файле _blog/article/views.py_ созданы контроллеры `article_list()`, `article_detail()`
* В _blog/templates/user_ создан шаблон **users.html**
* В файле _blog/user/views.py_ создан контроллер `user_list()`
* С помощью `url_for()` реализованы ссылки в шаблонах для навигации.
