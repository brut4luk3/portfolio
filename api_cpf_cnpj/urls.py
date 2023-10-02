from django.urls import path

from . import views

app_name = 'api_cpf_cnpj'

urlpatterns = [
    path('', views.index_api_cpf_cnpj, name='index_api_cpf_cnpj'),
]