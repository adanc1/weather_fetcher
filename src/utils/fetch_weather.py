import os
from datetime import datetime, timezone

import pandas as pd
import requests
import requests.exceptions as requests_exceptions
from decouple import config

from .path_config import API_PATH, WEATHER_CSV

CITY = 'Lviv'
UNITS = 'metric'


def get_weather_data():
    try:
        result = requests.get(
            API_PATH,
            params={'q': CITY, 'appid': config('API_KEY'), 'lang': 'ua', 'units': UNITS}
        )
        data = result.json()
        main = data['weather'][0]['main']
        temp = data['main']['temp']
        wind_speed = data['wind']['speed']
        data = {
            'temperature': [temp],
            'main': [main],
            'date': [datetime.now(timezone.utc).date()],
            'wind_speed': [wind_speed]
        }
        df = pd.DataFrame(data)
        if os.path.exists(WEATHER_CSV):
            df.to_csv(WEATHER_CSV, mode='a', index=False, header=False)
        else:
            df.to_csv(WEATHER_CSV, mode='w', index=False)
        print("Data appended successfully.", df)
    except requests_exceptions.ConnectionError:
        print(f"Could not connect to {API_PATH}.")
