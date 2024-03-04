from datetime import datetime
from typing import Union

import aiohttp
from environs import Env


async def get_weather_for_current_city(city: Union[str] = None) -> dict:
    env = Env()
    env.read_env()
    api_key = env("WEATHER_API_KEY")
    url = (f'https://api.openweathermap.org/data/2.5/weather?q={city}&'
           f'lang=ru&units=metric&APPID={api_key}')
    async with aiohttp.ClientSession() as session:
        request = await session.get(url)
        response = await request.json()
        if response["cod"] == 200:
            response_dict = {
                "temperature": response["main"]["temp"],
                "humidity": response["main"]["humidity"],
                "description": response["weather"][0]["description"],
                "sunrise": datetime.fromtimestamp(
                    response["sys"]["sunrise"]).strftime("%H:%M:%S %d-%m-%Y"),
                "sunset": datetime.fromtimestamp(
                    response["sys"]["sunset"]).strftime("%H:%M:%S %d-%m-%Y"),
                "wind_speed": response["wind"]["speed"],
                "wind_gust": response["wind"]["gust"],
                "country": response["sys"]["country"]

            }
            return response_dict
        return None
