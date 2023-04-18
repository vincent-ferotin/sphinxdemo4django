"""
Patrons d'URLs de l'`app`.
"""
from django.urls import path

from . import views


#: Liste des patrons d'URLs gérés par l'`app`.
#:
#: .. seealso:: :external+django:ref:`how-django-processes-a-request`
urlpatterns = [
    path("", views.index, name="hello_index"),
]
