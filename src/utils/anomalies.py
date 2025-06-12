from dal import crud
from .tg_message_handler import send_message

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

    if (float(current_temp) - float(avg_temp)) < 10:
        crud.insert_anomalies(city_id, current_temp, avg_temp, source_id)
        send_message(
            f"⚠️ <b>Anomaly detected</b>\n"
            f"🌡️ Current temperature: {current_temp:.1f}°C\n"
            f"📊 7-day average: {avg_temp:.1f}°C\n"
            f"🧥 <i>It might be unusual today — consider dressing accordingly!</i>"
        )

    print("Anomalies has been checked successfully.")

