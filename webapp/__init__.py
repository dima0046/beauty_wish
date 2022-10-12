from flask import Flask,  render_template

from webapp.model import db, Products
from webapp.podrujka_parsing import get_podrujka_make


def create_app():
    app = Flask(__name__) #Новое приложение Фласк. Передаём имя текущего приложения
    #app.run(debug=True)
    app.config.from_pyfile('config.py')
    db.init_app(app) #инициализируем нашу БД

    @app.route('/') #декоратор
    def index():
        page_title = "Продукты"
        #weather = weather_by_city(app.config["WEATHER_DEFAULT_CITY"])
        #get_podrujka_make()
        product_list = Products.query.all()

        return render_template('index.html', page_title=page_title, product_list=product_list)
    return app