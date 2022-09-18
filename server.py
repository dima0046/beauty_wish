from flask import Flask

app = Flask(__name__) #Новое приложение Фласк. Передаём имя текущего приложения

@app.route('/') #декоратор
def index():
    return 'Привет!'

if __name__ == '__main__':
    app.run()
