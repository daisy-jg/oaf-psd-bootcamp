import requests
from abc import ABC, abstractmethod

class AbstractDataService(ABC):
    @abstractmethod
    def getWeatherForecast(self, latitude, longitude):
        pass

class WeatherAPIService(AbstractDataService):
    def getWeatherForecast(self, latitude, longitude):
        url = f"https://api.open-meteo.com/v1/forecast?latitude=41.85&longitude=-87.65&hourly=temperature_2m"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Failed to fetch weather forecast")

class MockedWeatherService(AbstractDataService):
    def getWeatherForecast(self, latitude, longitude):
        return {
            "latitude": latitude,
            "longitude": longitude,
            "hourly": {
            }
        }

class WeatherDataHandler:
    def __init__(self, data_service):
        self.data_service = data_service

    def fetchWeatherForecast(self, latitude, longitude):
        return self.data_service.getWeatherForecast(latitude, longitude)