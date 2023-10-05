"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/users/')),
    path('users/', include('users.urls')),
    path('registration/', include('django.contrib.auth.urls')),
    path('register/', include('register.urls')),
    path('api_compara_datas/', include('api_compara_datas.urls')),
    path('api_geolocation/', include('api_geolocation.urls')),
    path('api_informa_dia_util/', include('api_informa_dia_util.urls')),
    path('api_replace_text/', include('api_replace_text.urls')),
    path('api_cpf_cnpj/', include('api_cpf_cnpj.urls')),
    path('api_telefone_latam/', include('api_telefone_latam.urls')),
]
