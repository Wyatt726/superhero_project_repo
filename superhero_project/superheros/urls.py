from django.urls import path

from . import views

app_anme = 'superheros'
urlpattern = [
    path('', views.index, name='index'),
    path('<int:hero_id>/'), views.detail, name='detail'),
    path('new/', views.create, name='create')

]

