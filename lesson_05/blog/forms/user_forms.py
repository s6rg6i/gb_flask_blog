from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, PasswordField


class UserLoginForm(FlaskForm):
    login = StringField("Логин", [validators.DataRequired(), ])
    password = PasswordField("Пароль", [validators.DataRequired(), ])
    submit = SubmitField('Авторизоваться')


class UserRegisterForm(FlaskForm):
    login = StringField("Логин", [validators.DataRequired(), ])
    name = StringField("Полное имя", [validators.DataRequired(), ])
    email = StringField("Е-мейл", [validators.DataRequired(), validators.Email()], )
    password = PasswordField("Пароль", [validators.DataRequired(), validators.EqualTo("confirm")], )
    confirm = PasswordField("Подтверждение пароля", [validators.DataRequired(), ])
    submit = SubmitField('Зарегистрироваться')
