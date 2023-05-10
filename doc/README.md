<!--
NB: Les niveaux de titres sont incrémentés de 1, car le contenu du présent README
est inclus dans un autre document de la documentation.
-->

## Introduction

La présente documentation a pour but de documenter le projet `sphinxdemo`,
de démonstration d'usage possible de [Sphinx][sphinx] pour un `projet` [Django][django].
Pour un non-contributeur au présent projet, les sous-répertoires d'intérêt sont les suivants:

*   ``doc/html/``: documentation au format HTML (site web statique complet)


## Formats et outils

La documentation HTML est générée par l'outil de documentation [Sphinx][sphinx],
qu'on aura pris soin d'installer par ailleurs pour contribuer au projet
comme à la présente documentation (cf. section suivante).
Les sources de la documentation sont disponibles dans le sous-répertoire ``doc/src/``,
au format [reStructuredText][reST] que comprend *Sphinx*:
ce sont des simples [fichiers texte][texte].

La génération de la sortie HTML est commandée par le `Makefile`
à la racine du répertoire de la documentation (``doc/Makefile``).


## Dépendances de la documentation

La génération de sortie HTML de la présente documentation se fait grâce à
la série de logiciels tiers spécifiés dans le fichier ``doc/pip-requirements.txt``.

On pourra les installer de manière additionnelle dans le *virtualenv* du projet
(cf. son `README`).
Sous Unix, cela peut se faire par exemple avec:

```{code-block} shell
# On suppose le réemploi du virtualenv du projet 'sphinxdemo', situé dans l'arborescence
# système ici: /opt/virtualenvs/sphinxdemo/
# Installation des dépendances propres à la documentation
$ /opt/virtualenvs/sphinxdemo/bin/python -m pip install -r doc/pip-requirements.txt
```


## Développement de la documentation et génération de sortie HTML

La documentation offre, à travers son ``doc/Makefile``, les tâches les plus courantes.
Vous pouvez les lister en invoquant (GNU) `make` sans argument,
ce qui affichera son aide succinte intégrée, notamment la liste des *cibles*
(ici des "commandes") offertes.

Une opération courante, par exemple ``html`` pour générer la sortie HTML,
s'invoquera en spécifiant à `make` cette *cible* particulière comme argument:

```{code-block} shell
$ cd doc && make html
```


## Structure détaillée du projet

La documentation du projet est composée de matériel pour [Sphinx][sphinx],
et des utilisateurs n'utilisant aucun de ces deux outils:

*   le matériel pour *Sphinx* comprend:

    *   le fichier ``doc/Makefile``, qui contient les cibles pour générer
        les formats de sortie,
    *   le répertoire ``doc/src/``, qui comprend les sources [reStructuredText][reST]
        et la configuration nécessaires à *Sphinx* pour générer la sortie,
    *   le répertoire ``doc/doctrees/``, utilisé en interne par *Sphinx*,

*   la sortie HTML, utilisables par les lecteurs du projet,
    est enregistrée dans le sous-répertoire ``doc/html/``.

Cette structure, cette arborescence permet donc d'enregistrer et versionner
tant les sources de la documentation, ses formats de sortie, et la configuration
de la machine virtuelle permettant la transformation des premières en
ces secondes, et autorisant des utilisateurs non techniciens à accéder
néanmoins au contenu de la documentation
-- pourvu bien sûr qu'on prenne soin de systématiquement générer et versionner
toutes les sorties à chaque modification des sources.


## Utilisation

Maintenant que la configuration requise a été réalisée, il est facile
d'utiliser le *virtualenv* pour demander à [Sphinx][sphinx] de générer
la sortie HTML.

Les cibles principales du ``doc/Makefile`` sont listées dans la sortie de `help`:

```{code-block} shell
$ cd doc
$ make help
```

(Par la suite, on supposera le répertoire courant où sont exécutées les commandes
celui de la documentation: ``doc/``.)

Il est possible d'enchaîner les cibles, pour réaliser l'exécution
de plusieurs recettes en une même invocation. Le patron d'invocation est le suivant:

```{code-block} shell
$ make TARGET1 [TARGET2 [...]]
```

Si le *virtualenv* est `activé`, il n'est pas besoin de spécifier le chemin du binaire
`sphinx-build` utilisé par ``doc/Makefile``; dans le cas inverse où le *virtualenv*
ne serait pas activé, on prendra soin de surcharger la variable d'environnement `SPHINXBUILD`
avec le chemin de ce binaire:

```{code-block} shell
$ SPHINXBUILD="/opt/virtualenvs/sphinxdemo/bin/sphinx-build" make html
```

Pour regénérer l'intégralité des sorties, utiliser la cible `all`:

```{code-block} shell
$ make all
```


[django]: https://www.djangoproject.com/
[reST]:     http://docutils.sourceforge.net/rst.html
[Sphinx]:   https://www.sphinx-doc.org/
[texte]:    https://fr.wikipedia.org/wiki/Fichier_texte

