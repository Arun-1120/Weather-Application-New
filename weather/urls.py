from django.contrib import admin
from django.urls import path
from weather import views  # Import your views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.weather_view, name='home'),  # Your weather view
    # Add other URL patterns here
]

# Add static file handling
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
