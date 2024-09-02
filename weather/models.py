from django.db import models


class WeatherData(models.Model):
    city = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    humidity = models.FloatField()
    weather_condition = models.CharField(max_length=100)

    class Meta:
        indexes = [
            models.Index(fields=['city', 'timestamp']),
        ]
