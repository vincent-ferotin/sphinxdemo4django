"""
Configuration de patrons d'URLs pour le `projet`.
"""
from django.urls import (
    include,
    path,
)


#: Liste des patrons d'URLs gérés par le `projet`.
#:
#: Cette liste est uniquement constituée des patrons d'URLs définis
#: par l'`app` ``hello``: :mod:`hello.urls`.
#:
#: .. seealso:: :external+django:ref:`how-django-processes-a-request`
urlpatterns = [
    path('', include("hello.urls")),
]
