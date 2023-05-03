<!--
NB: Les niveaux de titres sont incrémentés de 1, car le contenu du présent README
est inclus dans un autre document de la documentation.
-->

## Résumé

### Project's summary

This project aims to be a demonstration of [Sphinx][sphinx] usage
for [Django][django] projects.
It is aimed for small French team not fluent at reading and/or writing English,
so all other documentation content (including tail of this README)
and sources files target this language.
It is specifically not intend to promote any "good practices" regarding
development of a `Django` project.


### Résumé du projet

Le présent projet se veut une brêve démonstration d'usage de [Sphinx][sphinx]
pour un projet [Django][django]. Il suppose une petite équipe travaillant
en français principalement, d'où ce choix de langue pour les commentaires
du code comme le contenu de la documentation.
Particulièrement, il n'est en aucun cas une préconisation quant à
de quelconques bonnes pratiques pour le bon développement d'un projet `Django`.


## Structure du projet

Ce projet [Django][django] est composé, outre sa documentation, d'une `app Django`
nommée ``hello``, et d'un `projet Django` nommé ``sphinxdemo`` reposant sur cette `app`.

- ``data/``:
  répertoire où sera stockée la base [SQLite][sqlite] par défaut du projet
- ``doc/``:
  répertoire de la documentation gérée par [Sphinx][sphinx]
- ``hello/``:
  sources [Python][python] de l'`app` [Django][django] principale: ``hello``
- ``sphinxdemo``:
  sources [Python][python] du `projet` [Django][django]: ``sphinxdemo``
- ``manage.py``:
  fichier de commandes [Django][django] pour gérer le projet ``sphinxdemo``
- ``pip-requirements.txt``:
  fichier de dépendances tierces [Python][python] explicites du projet.


## Démarrage rapide du projet ("quickstart")

### Création et peuplement d'un `virtualenv` dédié

Les dépendances du projet, sous forme de `packages` [Python][python] installables
via [pip][pip], sont listées dans son fichier ``pip-requirements.txt``.
On les installera dans un [virtualenv][venv] dédié:

```{code-block} shell
# Création d'un nouveau virtualenv dédié, grâce au module 'venv' de la bibliothèque standart
# (adaptez le chemin du nouveau virtualenv à votre usage):
$ python3 -m venv /opt/virtualenvs/sphinxdemo
# Mise à jour des packages de packaging de ce virtualenv:
$ /opt/virtualenvs/sphinxdemo/bin/python3 -m pip install --upgrade setuptools
$ /opt/virtualenvs/sphinxdemo/bin/python3 -m pip install --upgrade pip
$ /opt/virtualenvs/sphinxdemo/bin/python3 -m pip install --upgrade wheel
# Installation des dépendances du présent projet:
$ /opt/virtualenvs/sphinxdemo/bin/python3 -m pip install -r ./pip-requirements.txt
```


### Création de la base `SQLite` du projet

Si le fichier ``sphinxdemo/settings.py`` n'a pas été alteré, le projet ``sphinxdemo``
est configuré pour reposer par défaut sur une base de données [SQLite][sqlite],
au démarrage inexistante, qui sera stockée dans le répertoire ``data/``.
On la créera, en appliquant automatiquement les `migrations` de schéma spécifiées
dans le projet, par la commande ``migrate`` de ``./manage.py``:

```{code-block} shell
$ ls -a ./data
.  ..  .gitkeep
# Création de la base de données SQLite, et application des migrations du projet:
$ /opt/virtualenvs/sphinxdemo/bin/python3 ./manage.py migrate
Operations to perform:
  Apply all migrations: auth, contenttypes, hello, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
[...]
$ ls -l ./data
-rw-r--r-- 1 vincent vincent 126976  3 mai   21:15 database.sqlite3
```


### Lancement du serveur web de développement

Pour lancer le serveur web de *développement*, on appelera la commande ``runserver``
de ``./manage.py``:

```{code-block} shell
# Lancement du server web de dev.:
$ /opt/virtualenvs/sphinxdemo/bin/python3 ./manage.py runserver
[...]
Django version 4.2.1, using settings 'sphinxdemo.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Le projet est alors accessible en local via un navigateur web à l'URL par défaut:
http://127.0.0.1:8000/


[django]: https://www.djangoproject.com/
[pip]:    https://pip.pypa.io/
[python]: https://www.python.org/
[sphinx]: https://www.sphinx-doc.org/
[sqlite]: https://docs.python.org/3/library/sqlite3.html
[venv]:   https://docs.python.org/3/library/venv.html
