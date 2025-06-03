from dal import crud

CITY = 'Lviv'

def analyze_weather_data():
    try:
        rows = crud.get_daily_stats()
        if not rows:
            print("No data to analyze.")
            return
        city_id = crud.get_or_create_city(CITY)
        for date, avg_temp, avg_wind, avg_hum in rows:
            crud.insert_daily_stats(date, city_id, avg_temp, avg_wind, avg_hum)

        print("Daily statistics saved")

    except Exception as e:
        print(f"Error: {e}")
