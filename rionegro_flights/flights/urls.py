from django.urls import path 
from .import views

urlpatterns = [
path('registrar/', views.registrar_vuelos, name = 'registrar_vuelos'),
path('listar/', views.listar_vuelos, name= 'listar_vuelos'),
path('estadisticas/', views.estadisticas_vuelos, name= 'estadisticas_vuelos'),

]