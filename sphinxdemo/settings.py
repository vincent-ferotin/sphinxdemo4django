"""
Configuration d'une instance de projet Django pour l'`app` `hello`.

.. seealso:: :external+django:ref:`django-settings-module`
"""

from pathlib import Path


#: Chemin du répertoire racine du dépôt `git` du présent projet
#: (:external+python:class:`pathlib.Path`).
BASE_DIR = Path(__file__).resolve().parent.parent
# Build paths inside the project like this: BASE_DIR / 'subdir'.

#: Chemin du répertoire de données du `projet` `Django` (ou `instance`)
#: (:external+python:class:`pathlib.Path`).
#:
#: C'est dans ce répertoire que pourrait être stockée par exemple
#: :data:`la base SQLite <DATABASES>`.
DATA_DIR = BASE_DIR / 'data'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

#: Clef de chiffrement pour les données du `projet`, par ex. les `cookies web`
#: (`str`).
#:
#: La valeur de cette variable est à changer à chaque `instanciation` du `projet`!
#:
#: .. warning:: **Securité**\ : La clef utilisée en production doit évidemment rester secrète!
#:
#: .. seealso:: :external+django:setting:`SECRET_KEY`
SECRET_KEY = 'django-insecure-dw3&1aos--n#1&^1v-z=ou8(i5is_sit@$=p_l0+5nh1kbtrqz'

#: Activation du mode `debug` de `Django` (`bool`).
#:
#: Positionner à ``True`` est utile en phase de développement.
#:
#: .. warning:: **Securité**\ : En production, doit être positionnée à ``False``!
#:
#: .. seealso:: :external+django:setting:`DEBUG`
DEBUG = True  # SECURITY WARNING: don't run with debug turned on in production!

#: Liste blanche d'hôtes autorisés à se connecter au projet.
#:
#: Laisser vide pour un site publique,
#: sinon expliciter les clients autorisés.
#:
#: .. seealso:: :external+django:setting:`ALLOWED_HOSTS`
ALLOWED_HOSTS = []


# Application definition

#: Liste des `apps` `Django` activées pour ce `projet` / cette `instance`
#: (`list` of `apps` paths or `config`).
#:
#: L'`app` principale "maison" est ``hello``, définie par sa configuration
#: :class:`hello.apps.HelloConfig`.
#:
#: Liste à adapter au déploiement de l'instance; dans le doute laisser telle quelle.
#:
#: .. seealso:: :external+django:setting:`INSTALLED_APPS`
INSTALLED_APPS = [
    'hello.apps.HelloConfig',

    # Default Django apps:
    #'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

#: Liste des `middlewares` `Django` activés pour ce `projet` / cette `instance`
#: (`list` of `middlewares` class paths).
#:
#: Liste à adapter au déploiement de l'instance; dans le doute laisser telle quelle.
#:
#: .. seealso:: :external+django:setting:`MIDDLEWARE`
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#: Chemin du module définissant les patrons d'URLs gérés par ce `projet` / cette `instance`
#: (`str` of `module` path).
#:
#: La première partie (ici ``'sphinxdemo'``) correspond
#: au :external+python:term:`package` du projet, et à adapter si besoin
#: à la configuration de votre déploiement.
#: La seconde partie (ici ``'urls'``) correspond au :external+python:term:`module`
#: ``sphinxdemo/urls.py``.
#:
#: .. seealso:: :ref:`urls`
ROOT_URLCONF = 'sphinxdemo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

#: Application :external+python:mod:`WSGI <wsgiref>` pour servir en `HTTP` le projet.
#:
#: La première partie (ici ``'sphinxdemo'``) correspond
#: au :external+python:term:`package` du projet, et à adapter si besoin
#: à la configuration de votre déploiement.
#: La seconde partie (ici ``'wsgi'``) correspond au :external+python:term:`module`
#: ``sphinxdemo/wsgi.py``.
#:
#: .. seealso:: :external+django:setting:`WSGI_APPLICATION`
WSGI_APPLICATION = 'sphinxdemo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

#: Configuration de la (ou les) base(s) de données du projet.
#:
#: Pour cette `app` `Django` très simple, il n'y a qu'une seule base de données
#: à configurer, nommée ``'default'``.
#:
#: Pour le développement de l'`app` comme pour un déploiement à petite échelle,
#: une base `SQLite` suffit amplement, et permet de se dispenser de monter et configurer
#: un serveur de bases de données dédié, comme `MariaDB` ou `PostgreSQL`.
#: Le chemin de la base est ici configuré par défaut pour avoir comme répertoire parent
#: :data:`DATA_DIR`, défini dans ce même fichier ``settings.py``.
#:
#: .. seealso:: :external+django:setting:`DATABASES`
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DATA_DIR / 'database.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

#: Fuseau horaire du projet
#: (`str` as :external+python:class:`valid IANA time zone key <zoneinfo.ZoneInfo>`).
#:
#: .. seealso:: :external+django:setting:`TIME_ZONE`
TIME_ZONE = 'Europe/Paris'

USE_I18N = False

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

#: .. seealso:: :external+django:setting:`STATIC_URL`
STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
