from datetime import date
from .base import get_db_cursor


def get_city_id(city: str) -> int:
    with get_db_cursor() as cur:
        cur.execute("SELECT id FROM location WHERE city = %s;", (city,))
        result = cur.fetchone()
    return result[0] if result else None


def insert_location(city: str) -> int:
    with get_db_cursor() as cur:
        cur.execute(
            """
            INSERT INTO location (city) 
            VALUES (%s);
            """
            ,
            (city,)
        )


def insert_weather_data(
    city_id: int,
    date_: date,
    temperature: float,
    humidity: float,
    wind_speed: float,
    weather_main: str
):
    with get_db_cursor() as cur:
        cur.execute(
            """
            INSERT INTO weather_data (city_id, date, temperature, humidity, wind_speed, weather_main)
            VALUES (%s, %s, %s, %s, %s, %s);
            """
            ,
            (city_id, date_, temperature, humidity, wind_speed, weather_main)
        )


def get_weather_data() -> list:
    with get_db_cursor() as cur:
        cur.execute("SELECT * FROM weather_data;")
        rows = cur.fetchall()
    return rows


def insert_daily_stats(
    report_date: date,
    city_id: int,
    avg_temp: float,
    max_wind: float,
    avg_hum: float
):
    with get_db_cursor() as cur:
        cur.execute(
            """
            INSERT INTO daily_weather_stats (report_date, city_id, avg_temp, max_wind, avg_hum)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (report_date, city_id, avg_temp, max_wind, avg_hum)
        )


def get_daily_stats() -> list:
    with get_db_cursor() as cur:
        cur.execute(
            """
            SELECT 
                date, 
                AVG(temperature) AS avg_temperature,
                MAX(wind_speed) AS max_wind_speed,
                AVG(humidity) AS avg_humidity
            FROM weather_data
            GROUP BY date;
            """
        )
        rows = cur.fetchall()
    return rows
