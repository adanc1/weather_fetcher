from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import date, datetime, UTC


class Location(SQLModel, table=True):
    __tablename__ = "location"

    id: Optional[int] = Field(default=None, primary_key=True)
    city: str = Field(max_length=100, nullable=False, unique=True)

    weather_data: Optional["WeatherData"] = Relationship(
        back_populates="city"
    )



class WeatherData(SQLModel, table=True):
    __tablename__ = "weather_data"

    id: Optional[int] = Field(default=None, primary_key=True)
    city_id: int = Field(foreign_key="location.id")
    date: date
    temperature: Optional[float] = None
    humidity: Optional[float] = None
    wind_speed: Optional[float] = None
    weather_main: Optional[str] = Field(default=None, max_length=50)
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    created_by: int = Field(default=1)

    city: Optional["Location"] = Relationship(
        back_populates="weather_data",
        sa_relationship_kwargs={'lazy': 'selectin'}
    )


class DailyWeatherStats(SQLModel, table=True):
    __tablename__ = "daily_weather_stats"

    id: Optional[int] = Field(default=None, primary_key=True)
    report_date: date
    city_id: int = Field(foreign_key="location.id")
    avg_temp: Optional[float] = None
    max_wind: Optional[float] = None
    avg_hum: Optional[float] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    created_by: int = Field(default=1)
