from flask import Flask,  render_template
from weather import weather_by_city


app = Flask(__name__) #Новое приложение Фласк. Передаём имя текущего приложения
#app.run(debug=True)

@app.route('/') #декоратор
def index():
    page_title = "Новости Python"
    weather = weather_by_city('Moscow,Russia')

    '''
    if weather:
        weather_text = f"Сегодня {weather['temp_C']}. Ощущается как {weather['FeelsLikeC']}!!!"
    else:
        weather_text = "Denied!"
    '''
    return render_template('index.html', page_title=page_title, weather=weather)

if __name__ == '__main__':
    app.run(debug=True)
