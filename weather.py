import requests

def weather_by_city(city_name):
    weather_url = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
    params1 ={
        "key": "e11d39f3169b4748b32153154221809",
        "q": city_name,
        "format": "json",
        "num_of_days": 1,
        "lang": "ru"
    }
    result = requests.get(weather_url, params=params1)
    weather = result.json()
    return weather

if __name__ == "__main__":
    w = weather_by_city("Moscow, Russia")
    print(w)