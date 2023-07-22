import os
from typing import Any

import requests
from dotenv import load_dotenv

# Load all envronment variables
load_dotenv()

API_KEY: str = os.getenv("API_KEY", "UnKnown")


class CityNotFoundError(Exception):
    pass


class WeatherService:
    # breakpoint()
    def __init__(self, city: str, api_key: str) -> None:
        self.api_key: str = api_key
        self.city: str = city
        self.full_weather_forecast: dict[str, Any] = {}
        self.url: str = f"http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}"

    def retrieve_forecast(self) -> None:
        response: dict[str, Any] = requests.get(self.url, timeout=5).json()
        if "main" not in response:
            raise CityNotFoundError(
                f"Couldn't find weather data. Check '{self.city}' if it exists and is correctly spelled.\n"
            )
        self.full_weather_forecast = response

    # def print_temp(self) -> None:
    #     self.retrieve_forecast()
    #     temp: float = self.full_weather_forecast["main"]["temp"] - 273.15
    #     print(f"The current temperature in {self.city} is {temp:.1f} °C.")

    @property
    def temperature(self) -> float:
        temperature = self.full_weather_forecast["main"]["temp"]
        return temperature - 273.15  # kelvin to Celcsius


if __name__ == "__main__":
    my_city = "Valencia"

    my_weather_client = WeatherService(city=my_city, api_key=API_KEY)
    my_weather_client.retrieve_forecast()
    print(f"The temperature in {my_city} today is {my_weather_client.temperature:.1f} °C.")
