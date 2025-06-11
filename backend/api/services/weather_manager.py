from fastapi import Depends
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import WeatherData, DailyWeatherStats
from db.session import get_session


class WeatherDataManager:
    def __init__(self, session: AsyncSession = Depends(get_session)):
        self.session = session

    async def get_authors(self, offset: int = 0, limit: int = 10):
        stmt = select(WeatherData).offset(offset).limit(limit)
        result = await self.session.scalars(stmt)
        return result.all()