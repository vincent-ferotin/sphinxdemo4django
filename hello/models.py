"""
Modèles `Django` de l'`app`.
"""
from django.db import models


#: Valeurs hardcodées de :class:`Message`, servant au peuplement
#: initiale de la base de données (`dict` of `str`\ : `str`).
PREPOPULATED_DATA = [
    {"value": "Hello, World!"},
    {"value": "Bye bye..."},
]

class Message(models.Model):
    """
    Message texte tout simple.
    """
    #: Valeur textuelle du message (`django.models.CharField`).
    value = models.CharField(max_length=255, unique=True)

    @staticmethod
    def prepopulate():
        """
        Peuplement de la base de données avec les premiers :class:`Message`
        construits d'après les valeurs de :data:`PREPOPULATED_DATA`.
        """
        # On s'assure qu'il n'existe pas déjà en base de messages enregistrés.
        if Message.objects.count() == 0:
            for data in PREPOPULATED_DATA:
                Message(**data).save()
