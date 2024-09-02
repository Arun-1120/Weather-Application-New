from django.shortcuts import render
from .models import WeatherData
from .utils import fetch_weather_data, calculate_average_temperature, calculate_humidity_trends, check_extreme_weather


def weather_view(request):
    city = request.GET.get('city', '')

    if city:
        temperature, humidity, weather_condition = fetch_weather_data(city)
        avg_temp = calculate_average_temperature(city)
        humidity_trend = calculate_humidity_trends(city)
        alert = check_extreme_weather(city)
    else:
        temperature = humidity = weather_condition = avg_temp = humidity_trend = alert = None

    context = {
        'city': city,
        'temperature': temperature,
        'humidity': humidity,
        'weather_condition': weather_condition,
        'avg_temp': avg_temp,
        'humidity_trend': humidity_trend,
        'alert': alert
    }

    return render(request, 'weather/weather.html', context)
