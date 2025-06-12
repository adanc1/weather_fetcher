from fastapi import APIRouter, Depends
from db.models import WeatherData, DailyWeatherStats
from ..services.weather_manager import WeatherDataManager
from ..services.daily_weather_manager import WeatherStatsManager
from schemas.weather_schema import WeatherDataPublic
from utils.filters import book_filters

router = APIRouter()


@router.get("weather-data/", response_model=list[WeatherDataPublic])
async def get_weather_data(
        offset: int = 0, limit: int = 10, filters: dict = Depends(book_filters),
        weather: WeatherDataManager = Depends(WeatherDataManager)
):
    weather_data = await weather.get_weather_data(offset=offset, limit=limit, filters=filters)
    return weather_data


@router.get("weather-stats/", response_model=list[DailyWeatherStats])
async def get_weather_data(
        offset: int = 0, limit: int = 10, weather: WeatherStatsManager = Depends(WeatherStatsManager)
):
    weather_data = await weather.get_weather_stats(offset=offset, limit=limit)
    return weather_data
