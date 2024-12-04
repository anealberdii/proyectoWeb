from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index, name = 'index'),
    path ('festivales/', views.lista_festivales, name = 'lista_festivales'),
    path ('interpretes/', views.lista_interpretes, name = 'lista_interpretes'),
    path ('promotores/', views.lista_promotores, name = 'lista_promotores'),
    path ('festival/<int:id>/', views.detalles_festival, name='detalles_festival'),
    path ('interprete/<int:id>', views.detalles_interprete, name = 'detalles_interprete'),
    path ('promotor/<int:id>', views.detalles_promotor, name = 'detalles_promotor'),
    path ('festival/<int:id>/comprarEntrada', views.formulario, name = 'formulario'),
]