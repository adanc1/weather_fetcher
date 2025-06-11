from fastapi import FastAPI
from api.endpoints.weather import router as weather_router


app = FastAPI()

app.include_router(weather_router, prefix="/weather", tags=["weather"])
