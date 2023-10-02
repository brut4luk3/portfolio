from django.urls import path

from . import views

app_name = 'api_informa_dia_util'

urlpatterns = [
    path('', views.index_api_informa_dia_util, name='index_api_informa_dia_util'),
]