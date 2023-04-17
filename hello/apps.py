"""
Configuration de l'`app` pour `Django`.
"""
from django.apps import AppConfig


class HelloConfig(AppConfig):
    """
    Config. de l'`app`.

    Le chemin de cette classe est à ajouter à `INSTALLED_APPS` pour inclure
    cette `app` à votre projet:

        .. code-block:: python
            :caption: settings.py

            INSTALLED_APPS = [
                # ...
                'hello.apps.HelloConfig',
                # ...
            ]

    """
    #: Nom de l'`app` (`str`).
    name = 'hello'

    #: Champ additionnel automatiquement inclus dans les `modèles` de l'`app`
    #: comme `id` (`django.db.models.Field`).
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        """
        Méthode appelée par un `hook` `Django` à la fin d'initialisation du projet,
        permettant l'exécution de code idoine une seule fois.

        Ici, on peuple la base de données avec des premières instances de `modèles`,
        via :meth:`hello.models.Message.prepopulate`.
        """
        # L'import se fait dans le corps même de la méthode, et non comme
        # d'habitude en tête du module, pour éviter une dépendance circulaire.
        from .models import Message

        Message.prepopulate()
