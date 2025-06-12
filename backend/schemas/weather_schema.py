from datetime import date, datetime
from typing import Optional
from sqlmodel import SQLModel
from db.models import WeatherData, Location


class LocationPublic(SQLModel):
    id: int
    city: str


class WeatherDataPublic(SQLModel):
    id: int
    city: LocationPublic
    date: date
    temperature: Optional[float] = None
    humidity: Optional[float] = None
    wind_speed: Optional[float] = None
    weather_main: Optional[str] = None
    created_at: datetime
    created_by: int