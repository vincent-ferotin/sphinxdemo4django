from django.db import models


# Hardcode initial model instances for the demo.
PREPOPULATED_DATA = [
    {"value": "Hello, World!"},
    {"value": "Bye bye..."},
]

class Message(models.Model):
    value = models.CharField(max_length=255, unique=True)

    @staticmethod
    def prepopulate():
        if Message.objects.count() == 0:
            for data in PREPOPULATED_DATA:
                Message(**data).save()
