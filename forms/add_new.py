from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField, StringField, FileField
from wtforms.validators import DataRequired


class Add_NewForm(FlaskForm):
    text = StringField('Имя')
    image = FileField('Выберете файл')
    submit = SubmitField('Сохранить Изменения')
