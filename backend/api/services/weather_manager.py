from fastapi import Depends
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import WeatherData
from db.session import get_session


class WeatherDataManager:
    def __init__(self, session: AsyncSession = Depends(get_session)):
        self.session = session

    async def get_weather_data(self, offset: int = 0, limit: int = 10, filters: list = None):
        stmt = select(WeatherData)
        if filters:
            stmt = stmt.where(*filters)
        stmt = stmt.offset(offset).limit(limit)
        result = await self.session.scalars(stmt)
        return result.all()