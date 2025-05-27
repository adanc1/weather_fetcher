import pandas as pd
from .path_config import ANALYSIS_CSV, WEATHER_CSV


def analyze_weather_data():
    try:
        df = pd.read_csv(WEATHER_CSV)
        df['date'] = pd.to_datetime(df['date'])
        grouped_data = df.groupby('date')[['temperature', 'wind_speed']].mean()
        grouped_data.to_csv(ANALYSIS_CSV, index=False)
        print(grouped_data)
    except FileNotFoundError:
        print('Could not find weather data')
