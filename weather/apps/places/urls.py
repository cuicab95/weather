from rest_framework import routers
from . import views
from django.urls import path
app_name = 'api'

router = routers.SimpleRouter()
urlpatterns = [
    path('get-weather-by-place/', views.GetWeatherByPlaceAPIView.as_view(), name='get-weather-by-place'),
]
urlpatterns = router.urls + urlpatterns
