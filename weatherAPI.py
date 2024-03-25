import requests
from abc import ABC, abstractmethod

class AbstractDataService(ABC):
    @abstractmethod
    def getWeatherForecast(self, latitude, longitude):
        pass

class WeatherAPIService(AbstractDataService):
    def getWeatherForecast(self, latitude, longitude):
        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            
            hourly_forecast = {
                "time": data.get("hourly", {}).get("time", []),
                "temperature_2m": data.get("hourly", {}).get("temperature_2m", [])
            }
            
            return hourly_forecast  
            
        else:
            raise Exception("Failed to fetch weather forecast")

class MockedWeatherService(AbstractDataService):
    def getWeatherForecast(self, latitude, longitude):
        hourly_forecast = {
            "time": [
                "2024-03-25T00:00",
                "2024-03-25T01:00",
                "2024-03-25T02:00",
            ],
            "temperature_2m": [
                6.1,
                5.5,
                5.2,
            ]
        }
        return {
            "latitude": latitude,
            "longitude": longitude,
            "hourly": hourly_forecast  
        }

class WeatherDataHandler:
    def __init__(self, data_service):
        self.data_service = data_service

    def fetchWeatherForecast(self, latitude, longitude):
        return self.data_service.getWeatherForecast(latitude, longitude)

    def fetchWeatherForecast(self, latitude, longitude):
        return self.data_service.getWeatherForecast(latitude, longitude)
