import os
from datetime import datetime, timezone

import requests
import requests.exceptions as requests_exceptions
from decouple import config
from psycopg2 import OperationalError

from .path_config import API_PATH
from dal import crud

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
        temp = data['main'].get('temp')
        humidity = data['main'].get('humidity')
        wind_speed = data['wind'].get('speed')
        date = datetime.now(timezone.utc).date()

        city_id = crud.get_city_id(CITY)
        if city_id is None:
            crud.insert_location(CITY)
            city_id = crud.get_city_id(CITY)

        crud.insert_weather_data(
            city_id=city_id,
            date_=date,
            temperature=temp,
            humidity=humidity,
            wind_speed=wind_speed,
            weather_main=main
        )
        print(f"Data inserted successfully.")
        for i in crud.get_weather_data():
            print(i)
    except requests_exceptions.ConnectionError:
        print(f"Could not connect to {API_PATH}.")
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error: {err}")
    except OperationalError as db_err:
        print(f"Database error: {db_err}")
