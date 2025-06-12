from fastapi import Query
from typing import Optional
from datetime import date
from db.models import WeatherData


def book_filters(
    city_id: Optional[int] = Query(None, description="City ID filter"),
    date_from: Optional[date] = Query(None, description="Start date (inclusive)"),
    date_to: Optional[date] = Query(None, description="End date (inclusive)")
):
    filters = []
    if city_id:
        filters.append(WeatherData.city_id == city_id)
    if date_from:
        filters.append(WeatherData.date >= date_from)
    if date_to:
        filters.append(WeatherData.date <= date_to)
    return filters
