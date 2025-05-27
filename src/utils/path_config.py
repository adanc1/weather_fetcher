import os
from pathlib import Path


BASE_DATA_DIR = Path(os.environ.get("DATA_DIR", "/app/data"))

WEATHER_CSV = BASE_DATA_DIR / "weather_data.csv"
ANALYSIS_CSV = BASE_DATA_DIR / "analyzed_data.csv"

API_PATH = 'https://api.openweathermap.org/data/2.5/weather'
