from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired


class UploadImageForm(FlaskForm):
    submit = SubmitField('Загрузить')
