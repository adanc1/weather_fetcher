from fastapi import APIRouter, Depends
from db.models import WeatherData
from ..services.weather_manager import WeatherDataManager

router = APIRouter()

@router.get("/", response_model=list[WeatherData])
async def get_weather_data(
    offset: int = 0, limit: int = 10, weather: WeatherDataManager = Depends(WeatherDataManager)
):
    weather_data = await weather.get_authors(offset=offset, limit=limit)
    return weather_data
