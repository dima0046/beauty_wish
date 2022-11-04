import email
import re
from flask import flash, render_template, redirect, url_for, Blueprint, request
from flask_login import current_user, login_user, logout_user, login_required
from flask_change_password import ChangePassword, ChangePasswordForm, SetPasswordForm
from webapp import user
from webapp.utils import get_redirect_target

# flash - позволяет передавать сообщения между route-ами
# redirect - делает перенаправление пользователя на другую страницу
# url_for - помогает получить url по имени функции, которая этот url обрабатывает

from webapp.db import db
from webapp.user.forms import LoginForm, RegistrationForm, EditForm
from webapp.user.models import User


blueprint = Blueprint('user', __name__, url_prefix='/users') # все адреса этой формы будут
                                                             # начинаться с /user (".../user/login" и т.д.)
# авторизация пользователя
@blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        redirect(url_for('products.index'))
    title = "Авторизация"
    login_form = LoginForm()
    return render_template('user/login.html', page_title=title, form=login_form)


@blueprint.route('/process-login', methods=['POST'])  # метод
def process_login():
    form = LoginForm()  # Создаём экземпляр формы
    if form.validate_on_submit():  # Если ошибки не возникло, но запрашиваем данные из БД
        user = User.query.filter_by(username=form.username.data).first()  # проверяем существование пользователя
        if user and user.check_password(form.password.data):  # Если пользователь существует, то проверяем пароль
            login_user(user,
                       remember=form.remember_me.data)  # логиним пользователя, если всё ок. Сохраняем значение чекбокса "Запомнить меня"
            
            return redirect(url_for('products.index'))
    flash('Неправильное имя пользователя или пароль')
    return redirect(url_for('user.login'))


@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('products.index'))


#Регистрация пользователя
@blueprint.route('/register')
def register():
    if current_user.is_authenticated:
        return redirect(url_for('products.index'))
    form = RegistrationForm()
    title = "Регистрация"
    return render_template('user/registration.html', page_title=title, form=form)


# Обработчик регистрации
@blueprint.route('/process-reg', methods=['POST'])
def process_reg():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data,
                         email=form.email.data, role='user')
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Вы успешно зарегистрировались!')
        return redirect(url_for('user.login'))
    else:
        for field, errors  in form.errors.items():
            flash('Ошибка в поле {}: {}'.format(
                getattr(form, field).label.text,
                errors
            ))
    return redirect(url_for('user.register'))





#Редактирование данных пользователя
@blueprint.route('/editaccount', methods=['GET', 'POST'])
def edit():
    title = "Редактирование данных"
    form = EditForm()
    form.email.data = current_user.email
    form.username.data = current_user.username
    #user_row = User.query.filter(User.id == current_user.id).first()
    if current_user.is_authenticated:
        if form.validate_on_submit():
            user_ = User.query.filter_by(id=current_user.id).first()
            user_.username = request.form['username']
            user_.email = request.form['email']
            if form.password.data != current_user.password:
                user_.set_password(form.password.data)
            
            db.session.commit()

            flash('Данные обновлены!')
            form.username.data = user_.username
            form.email.data = user_.email
            render_template('user/edit.html', page_title=title, form=form)
        else:
            for field, errors  in form.errors.items():
                flash('Ошибка в поле {}: {}'.format(
                    getattr(form, field).label.text,
                    errors
                ))            
        return render_template('user/edit.html', page_title=title, form=form)
    return redirect(url_for('user.login'))
