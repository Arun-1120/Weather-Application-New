# WeatherApp/urls.py

from django.contrib import admin
from django.urls import path
from weather import views  # Import your views here
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.weather_view, name='home'),  # URL pattern for your view
    # Add other URL patterns here
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
