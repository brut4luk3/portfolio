from django.urls import path

from . import views

app_name = 'api_compara_datas'

urlpatterns = [
    path('', views.index_api_compara_datas, name='index_api_compara_datas'),
]