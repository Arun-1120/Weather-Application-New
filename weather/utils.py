from django.db import models
from datetime import datetime, timedelta
from .models import WeatherData
from django.utils import timezone
import requests
API_KEY = '445e2242f6dbb61c2c2f7b4aef089b10'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'


def fetch_weather_data(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    weather_condition = data['weather'][0]['description']

    WeatherData.objects.create(
        city=city,
        temperature=temperature,
        humidity=humidity,
        weather_condition=weather_condition
    )

    return temperature, humidity, weather_condition


def calculate_average_temperature(city):
    now = datetime.now()
    past_24_hours = now - timedelta(hours=24)
    data = WeatherData.objects.filter(city=city, timestamp__gte=past_24_hours)

    if not data:
        return None

    average_temp = data.aggregate(models.Avg('temperature'))['temperature__avg']
    return average_temp


def calculate_humidity_trends(city):
    now = datetime.now()
    past_24_hours = now - timedelta(hours=24)
    data = WeatherData.objects.filter(city=city, timestamp__gte=past_24_hours)

    if not data:
        return None

    average_humidity = data.aggregate(models.Avg('humidity'))['humidity__avg']
    return average_humidity


def check_extreme_weather(city):
    temperature, humidity, condition = fetch_weather_data(city)

    if temperature > 35:  # Example threshold for extreme temperature
        return "Extreme heat alert!"
    elif temperature < 0:  # Example threshold for extreme cold
        return "Extreme cold alert!"
    elif humidity > 90:  # Example threshold for extreme humidity
        return "Extreme humidity alert!"

    return "Weather is normal."

