from django.apps import AppConfig


class HelloConfig(AppConfig):
    name = 'hello'
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        from .models import Message

        Message.prepopulate()
