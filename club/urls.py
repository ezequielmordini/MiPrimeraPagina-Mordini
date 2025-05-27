from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar-jugador/', views.agregar_jugador, name='agregar_jugador'),
    path('agregar-partido/', views.agregar_partido, name='agregar_partido'),
    path('agregar-noticia/', views.agregar_noticia, name='agregar_noticia'),
    path('buscar-jugador/', views.buscar_jugador, name='buscar_jugador'),
    path('registro-socio/', views.registrar_socio, name='registrar_socio'),
]
