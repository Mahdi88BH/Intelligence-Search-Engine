from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # Page d'accueil
    path('process/', views.process_query, name='process'), # URL pour l'API
]