import os
import asyncio
from dataclasses import dataclass
from typing import Any
from req_http import http_get, JSON
import requests
from dotenv import load_dotenv

# Load all envronment variables
load_dotenv()

API_KEY: str = os.getenv("API_KEY", "UnKnown")

@dataclass
class UrlTemplateClient:
    template: str

    async def get(self, data: dict[str, Any]) -> Any:
        url = self.template.format(**data)
        response = await http_get(url)
        return response


class CityNotFoundError(Exception):
    pass


async def get_capital(country: str) -> str:
    client = UrlTemplateClient(template="https://restcountries.com/v3/name/{country}")
    response = await client.get({"country": country})

    # The API can return multiple matches, so we just return the capital of the first match
    return response[0]["capital"][0]


async def get_forecast(city: str) -> dict[str, Any]:
    client = UrlTemplateClient(
        template=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    )
    response = await client.get({"city": city, "API_KEY": API_KEY})

    if "main" not in response:
        raise CityNotFoundError(
            f"Couldn't find weather data. Check '{city}' if it exists and is correctly spelled.\n"
        )
    return response


async def get_temperature(city: str)-> float:
    full_weather_forecast = await get_forecast(city)
    temperature = full_weather_forecast["main"]["temp"]
    return temperature - 273.15  # convert from Kelvin to Celsius


async def main() -> None:
    countries = ["United States of America", "Australia", "Japan", "France", "Brazil", "Spain"]

    for country in countries:
        capital = await get_capital(country)

        print(f"The capital of {country} is {capital}")

        weather_forecast = await get_forecast(capital)
        print(
            f"The current temperature in {capital} is {await get_temperature(weather_forecast):.1f} °C."
        )


if __name__ == "__main__":
    asyncio.run(main())
