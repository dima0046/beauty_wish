from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from webapp.user.models import User


class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()], render_kw={"class": "form-control"}) # DataRequired - обязательные поля
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-control"})
    remember_me = BooleanField('Запомнить меня', default=True, render_kw={"class": "form-check-input"})
    #email = StringField('Email', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить', render_kw={"class":"btn btn-primary"})

class RegistrationForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()], render_kw={"class": "form-control"})
    email = StringField('Email', validators=[DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-control"})
    password2 = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить!',render_kw={"class": "btn btn-primary"})
    
    def validate_username(self, username):
        user_count = User.query.filter_by(username=username.data).count()
        if user_count > 0:
            raise ValidationError('Пользователь с таким именем уже существует.')

    def validate_email(self, email):
        user_count = User.query.filter_by(email=email.data).count()
        if user_count > 0:
                raise ValidationError('Пользователь с таким Email уже существует.')

  
class EditForm(FlaskForm):
        username = StringField('Имя пользователя', validators=[DataRequired()], render_kw={"class": "form-control"})
        email = StringField('Email', validators=[DataRequired()], render_kw={"class": "form-control"})
        #oldpassword = PasswordField('Введите старый пароль', validators=[DataRequired()], render_kw={"class": "form-control"})
        #password = PasswordField('Введите новый пароль', validators=[DataRequired()], render_kw={"class": "form-control"})
        #password2 = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')], render_kw={"class": "form-control"})
        submit = SubmitField('Отправить!',render_kw={"class": "btn btn-primary"})


