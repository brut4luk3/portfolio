from django.urls import path

from . import views

app_name = 'api_geolocation'

urlpatterns = [
    path('', views.index_api_geolocation, name='index_api_geolocation'),
]