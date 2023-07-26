from dataclasses import dataclass
import asyncio
from req_http import http_get, JSON

from typing import Any


from dotenv import load_dotenv
import os
# Load all envronment variables
load_dotenv()

API_KEY: str = os.getenv("API_KEY", "UnKnown")


@dataclass
class UrlTemplateClient:
    template: str

    async def get(self, data: dict[str, Any]) -> JSON:
        url = self.template.format(**data)
        return await http_get(url)


class CityNotFoundError(Exception):
    pass


async def get_capital(country: str) -> str:
    client = UrlTemplateClient(template="https://restcountries.com/v3/name/{country}")
    response = await client.get({"country": country})

    # The API can return multiple matches, so we just return the capital of the first match
    return response[0]["capital"][0]  # type: ignore


async def get_forecast(city: str) -> JSON:
    client = UrlTemplateClient(
        template=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    )
    response = await client.get({"city": city})
    if "main" not in response:
        raise CityNotFoundError(
            f"Couldn't find weather data. Check '{city}' if it exists and is correctly spelled.\n"
        )
    return response


async def get_temperature(city: str) -> float:
    full_weather_forecast = await get_forecast(city)
    return full_weather_forecast["main"]["temp"] - 273.15  # type: ignore


async def get_capitals(countries: list[str]) -> list[str]:
    # for comprehension list using gather... Leading * since gather needs the resulting list disected
    return await asyncio.gather(*[get_capital(country) for country in countries])


async def get_temperatures(capitals: list[str]) -> list[float]:
    return await asyncio.gather(*[get_temperature(capital) for capital in capitals])


async def main() -> None:
    countries = ["United States of America", "Australia", "Japan", "France", "Brazil"]

    capitals = await get_capitals(countries)
    temperatures = await get_temperatures(capitals)

    for country, capital, temperature in zip(countries, capitals, temperatures):
        print(f"The capital of {country} is {capital}")
        print(f"The current temperature in {capital} is {temperature:.1f} °C.")


if __name__ == "__main__":
    asyncio.run(main())
