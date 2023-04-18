"""
Vues de l'app.
"""
from django.shortcuts import render

from .models import Message


def index(request):
    """
    Liste tous les :class:`Messages <hello.models.Message>` disponibles en base de données.
    """
    messages = Message.objects.all()
    return render(request, "index.html", {
        "messages": messages,
    })
