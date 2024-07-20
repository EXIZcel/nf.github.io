from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField, StringField, FileField
from wtforms.validators import DataRequired


class EditProfileForm(FlaskForm):
    name = StringField('Имя')
    about = StringField('О себе')
    image = FileField('Выберете файл')
    submit = SubmitField('Сохранить Изменения')
