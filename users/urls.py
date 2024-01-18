from django.urls import path

from . import views

app_name = 'users'

urlpatterns =[
    path('', views.index, name='index'),
    path('lang/en/', views.index_en, name='index_en'),
    path('login/', views.login, name='login'),
]