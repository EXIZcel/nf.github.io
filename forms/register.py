from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.fields.simple import StringField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password2 = PasswordField('Повторите пароль', validators=[DataRequired()])
    # image = FileField('Выберите аватарку')
    submit = SubmitField('Зарегистрироваться')

