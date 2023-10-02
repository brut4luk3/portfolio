from django.urls import path

from . import views

app_name = 'api_replace_text'

urlpatterns = [
    path('', views.index_api_replace_text, name='index_api_replace_text'),
]