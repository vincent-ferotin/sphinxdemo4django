"""
Configuration de l'`app` pour `Django`.
"""
from django.apps import AppConfig


class HelloConfig(AppConfig):
    """
    Config. de l'`app`.

    Le chemin de cette classe est à ajouter à :external+django:setting:`settings.INSTALLED_APPS
    <INSTALLED_APPS>` pour inclure cette `app` à votre projet:

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
    #: comme `id` (:external+django:mod:`django.db.models.Field
    #: <django.db.models.fields>`).
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        """
        Méthode appelée par un `hook` `Django` à la fin d'initialisation du projet,
        permettant l'exécution de code idoine une seule fois.

        Ici, on peuple la base de données avec des premières instances de `modèles`,
        via :meth:`hello.models.Message.prepopulate`.
        """
        # Les imports se font dans le corps même de la méthode, et non comme
        # d'habitude en tête du module, pour éviter une dépendance circulaire.
        from django.conf import settings

        from .dbutils import is_sqlite_empty
        from .models import Message

        if (settings.DATABASES['default']['ENGINE'] == 'django.db.backends.sqlite3') \
                and (not is_sqlite_empty()):
            Message.prepopulate()
