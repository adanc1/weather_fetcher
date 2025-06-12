from dal import crud

CITY = 'Lviv'


def get_anomalies():
    city_id = crud.get_city_id(CITY)

    rows = crud.get_weather_last_record(city_id=city_id)
    if not rows:
        print("No data to compare")
        return

    source_id = rows[0]
    city_id = rows[1]
    current_temp = rows[3]

    avg_temp = crud.get_last_7_days_avg(city_id)
    if avg_temp is None:
        print("No data for last 7 days")
        return

    if (float(current_temp) - float(avg_temp)) < 0:
        crud.insert_anomalies(city_id, current_temp, avg_temp, source_id)

    print("Anomalies has been checked successfully.")

