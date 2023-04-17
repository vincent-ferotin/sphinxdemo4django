"""
Patrons d'URLs de l'`app`.
"""
from django.urls import path

from . import views


#: Liste des patrons d'URLs gérés par l'`appp`.
urlpatterns = [
    path("", views.index, name="hello_index"),
]
