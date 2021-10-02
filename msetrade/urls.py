"""msetrade URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from alsat.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('user/', userindex, name='userindex' ),
    path('api/', apiindex, name='apiindex' ),
    path('buy/', buy, name='buy' ),
    path('sell/', sell, name='sell' ),
    path('settings/', settings, name='settings'),
    path('base/', base, name='base' ),
    path('anasayfa/', anasayfa, name='anasayfa' ),
    path('cuzdan/', cuzdan, name='cuzdan'),
    path('login/', login, name='login')
]
