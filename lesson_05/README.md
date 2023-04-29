### 5. WTForms. Регистрация и авторизация пользователя

---

#### Практическое задание:

* Создать форму регистрации с использованием WTForms.
* Добавить view для регистрации пользователя.
* Создать форму входа с использованием WTForms.
* Добавить view для авторизации пользователя.

#### Установлены зависимости:

* Flask-WTF 1.1.1 - [https://pypi.org/project/Flask-WTF/]
* email-validator 2.0.0.post2 - [https://pypi.org/project/email-validator/]

#### Выполнено

* Изменены пользовательские команды
  * Удалена команда инициализации БД `init-db` (используются миграции)
  * Изменена команда `create-user` на `set-superuser`
* Включаем в _config.py_ защиту от csrf в формы `WTF_CSRF_ENABLED = True`
* Формы:
  * В модуле _blog/forms/user_forms.py_ создана форма регистрации `UserRegisterForm`
  * В файле _blog/templates/macro/field_macro.html_ создан макрос `render_field(field)`
  * В папке _blog/templates/auth/_ создан шаблон для регистрации _register.html_ и 
    логина _login.html_
  * В файле _blog/auth/views/py_ создан контроллер  `register()` и `login()` 
    для отображения формы регистрации и логина.
