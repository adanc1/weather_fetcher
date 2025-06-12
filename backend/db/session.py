from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from decouple import config

DB_URI = f"postgresql+asyncpg://{config('DB_USER')}:{config('DB_PASSWORD')}@{config('DB_HOST')}:5432/{config('DB_NAME')}"
engine = create_async_engine(DB_URI)
SessionLocal = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_session():
    async with SessionLocal() as session:
        yield session
