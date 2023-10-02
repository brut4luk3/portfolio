from django.urls import path

from . import views

app_name = 'api_telefone_latam'

urlpatterns = [
    path('', views.index_api_telefone_latam, name='index_api_telefone_latam'),
]