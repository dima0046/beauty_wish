import os


basedir = os.path.abspath(os.path.dirname(__file__))


WEATHER_DEFAULT_CITY = "Moscow, Russia"
WEATHER_API_KEY = "e11d39f3169b4748b32153154221809"
WEATHER_URL = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, '..', 'webapp.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False