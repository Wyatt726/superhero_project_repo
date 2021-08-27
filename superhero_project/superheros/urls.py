from django.urls import path

from . import views

app_anme = 'superheros'
URLPattern = [
    path('index/', views.index, name='index')
]