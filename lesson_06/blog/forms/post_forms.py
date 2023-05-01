from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, TextAreaField, SelectField


from blog.models import Category


class CreatePostForm(FlaskForm):
    title = StringField('Заголовок поста', [validators.DataRequired()])
    content = TextAreaField('Содержание поста', )
    category = SelectField('Выберите категорию поста')
    submit = SubmitField('Создать')

    def __init__(self, *args, **kwargs):
        super(CreatePostForm, self).__init__(*args, **kwargs)
        self.category.choices = [(ctg.id, ctg.name) for ctg in Category.query.all()]



