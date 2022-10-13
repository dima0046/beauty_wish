from flask import Flask,  render_template, flash, redirect, url_for

# flash - позволяет передавать сообщения между route-ами
# redirect - делает перенаправление пользователя на другую страницу
# url_for - помогает получить url по имени функции, которая этот url обрабатывает

from flask_login import LoginManager, current_user, login_required,login_user, logout_user

from webapp.forms import LoginForm
from webapp.model import db, Products, User
from webapp.podrujka_parsing import get_podrujka_make


def create_app():
    app = Flask(__name__) #Новое приложение Фласк. Передаём имя текущего приложения
    #app.run(debug=True)
    app.config.from_pyfile('config.py')
    db.init_app(app) #инициализируем нашу БД

    # Управление авторизацией пользователя
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "login"

    # Функция, которая будет получать по id нужного пользователя.
    # При каждом заходе на страницу будет из сессионного cookie пользовательский id
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id) # Запрос к БД

    @app.route('/') #декоратор
    def index():
        page_title = "Beauty Wish"
        #weather = weather_by_city(app.config["WEATHER_DEFAULT_CITY"])
        #get_podrujka_make()
        product_list = Products.query.all()
        return render_template('index.html', page_title=page_title, product_list=product_list)

    @app.route('/login')
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        title = "Авторизация"
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)

    @app.route('/process-login', methods=['POST']) # метод
    def process_login():
        form = LoginForm() # Создаём экземпляр формы
        if form.validate_on_submit(): # Если ошибки не возникло, но запрашиваем данные из БД
            user = User.query.filter_by(username=form.username.data).first() # проверяем существование пользователя
            if user and user.check_password(form.password.data): # Если пользователь существует, то проверяем пароль
                login_user(user) # логиним пользователя, если всё ок
                flash('Вы вошли на сайт')
                return redirect(url_for('index'))
        flash('Неправильное имя пользователя или пароль')
        return redirect(url_for('login'))

    @app.route('/logout')
    def logout():
        logout_user()
        return redirect(url_for('index'))


    @app.route('/admin')
    @login_required
    def admin_index():
        if current_user.is_admin:
            return 'Привет, админ!'
        else:
            return 'Ты не админ!'

    return app