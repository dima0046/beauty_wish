from flask import flash, render_template, redirect, url_for, Blueprint
from flask_login import current_user, login_user, logout_user

# flash - позволяет передавать сообщения между route-ами
# redirect - делает перенаправление пользователя на другую страницу
# url_for - помогает получить url по имени функции, которая этот url обрабатывает

from webapp.user.forms import LoginForm
from webapp.user.models import User

blueprint = Blueprint('user', __name__, url_prefix='/users') # все адреса этой формы будут
                                                             # начинаться с /user (".../user/login" и т.д.)

@blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
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
            flash('Вы вошли на сайт')
            return redirect(url_for('index'))
    flash('Неправильное имя пользователя или пароль')
    return redirect(url_for('user.login'))


@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
