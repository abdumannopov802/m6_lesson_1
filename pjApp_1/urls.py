from django.contrib import admin
from .views import *
from django.urls import path

urlpatterns = [
    path('', sayhello),
    path('main', mainview),
    path('uzbekistan/', uzbekistan),
    path('jahon', jahon),
    path('iqtisodiyot', iqtisodiyot),
    path('jamiyat', jamiyat),
    path('fan/texnika', fan_texnika),
    path('sport', sport),
    path('nuqtainazar', nuqtainazar),
    path('audio', audio),
]