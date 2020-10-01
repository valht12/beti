from django.urls import path
from . import views
from .views import home

urlpatterns = [
    path('', views.home, name='home'),
    path('home2/', views.home2, name='home2'),
    path('blog/', views.blog, name='blog'),
    path('impuestos/', views.impuestos, name='impuestos'),
    path('finanzas/', views.finanzas, name='finanzas'),
    path('legal/', views.legal, name='legal'),
    path('opciones/', views.opciones, name='opciones'),
    path('terminos/', views.terminos, name='terminos'),
    path('politica/', views.politica, name='politica'),
]

