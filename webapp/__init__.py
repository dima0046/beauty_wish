from flask import Flask, render_template
from flask_login import LoginManager, current_user, login_required


from webapp.user.forms import LoginForm
from webapp.model import db, Products
from webapp.user.models import User
from webapp.admin.views import blueprint as admin_blueprint
from webapp.user.views import blueprint as user_blueprint
from webapp.podrujka_parsing import get_podrujka_make


def create_app():
    app = Flask(__name__)  # Новое приложение Фласк. Передаём имя текущего приложения
    # app.run(debug=True)
    app.config.from_pyfile('config.py')
    db.init_app(app)  # инициализируем нашу БД

    # Управление авторизацией пользователя
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "user.login"
    app.register_blueprint(user_blueprint)
    app.register_blueprint(admin_blueprint)

    # Функция, которая будет получать по id нужного пользователя.
    # При каждом заходе на страницу будет из сессионного cookie пользовательский id
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)  # Запрос к БД

    @app.route('/')  # декоратор
    def index():
        page_title = "Beauty Wish"
        # weather = weather_by_city(app.config["WEATHER_DEFAULT_CITY"])
        # get_podrujka_make()
        product_list = Products.query.all()
        return render_template('products/index.html', page_title=page_title, product_list=product_list)


    return app
