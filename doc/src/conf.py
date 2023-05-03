# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
from pathlib import Path
import os
import sys

import django


# Let Django apps and custom Sphinx extensions accessible through sys.path.
_this_filepath = Path(os.path.realpath(__file__))
_sphinxext_dirpath = _this_filepath.parent.parent / 'sphinxext'
_apps_dirpath = _this_filepath.parent.parent.parent
sys.path[0:0] = [
    str(_apps_dirpath),
    str(_sphinxext_dirpath),
]

# Setup Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'sphinxdemo.settings'
django.setup()


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SphinxDemo'
author = 'Vincent Férotin'
copyright = f'2023, {author}'
release = '0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # custom
    #   Voir https://stackoverflow.com/questions/13387125/how-to-link-with-intersphinx-to-django-specific-constructs-like-settings#13663325
    'intersphinx_djangodocs',

    # built-in
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',

    # third-party
    'myst_parser',
]

# extensions dedicated configuration:
# - sphinx.ext.todo:
todo_include_todos = True
# - sphinx.ext.intersphinx:
_django_version = '4.2'
_django_doc = f'https://docs.djangoproject.com/en/{_django_version}/'
intersphinx_mapping = {
    'django': (_django_doc, f'{_django_doc}_objects/'),
    'python': ('https://docs.python.org/3', None),
}
# - MyST-Parser:
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = []

language = 'fr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'library'
html_static_path = ['_static']
html_copy_source = False

