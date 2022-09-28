import requests
from flask import current_app # Позволяет обращаться к текущему flask приложению

def weather_by_city(city_name):
    weather_url = current_app.config['WEATHER_URL']
    params1 ={
        "key": current_app.config['WEATHER_API_KEY'],
        "q": city_name,
        "format": "json",
        "num_of_days": 1,
        "lang": "ru"
    }
    try:
            result = requests.get(weather_url, params=params1)
            result.raise_for_status() #Перехватывает 4хх и 5хх ошибки
            weather = result.json()
            print(weather)
            if 'data' in weather:
                if 'current_condition' in weather['data']:
                    try:
                        return weather['data']['current_condition'][0]
                    except(IndexError, TypeError):
                        return False
    except(requests.RequestException, ValueError):
        print('Net error')
        return False
    return False

if __name__ == "__main__":
    w = weather_by_city("Moscow, Russia")
    print(w)