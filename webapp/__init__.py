from flask import Flask,  render_template

from webapp.weather import weather_by_city
from webapp.python_org_news import get_python_news


def create_app():
    app = Flask(__name__) #Новое приложение Фласк. Передаём имя текущего приложения
    #app.run(debug=True)
    app.config.from_pyfile('config.py')

    @app.route('/') #декоратор
    def index():
        page_title = "Новости Python"
        weather = weather_by_city(app.config["WEATHER_DEFAULT_CITY"])
        news_list = get_python_news()

        '''
        if weather:
            weather_text = f"Сегодня {weather['temp_C']}. Ощущается как {weather['FeelsLikeC']}!!!"
        else:
            weather_text = "Denied!"
        '''
        return render_template('index.html', page_title=page_title, weather=weather, news_list=news_list)
    return app