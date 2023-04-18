# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
from pathlib import Path
import os
import sys

import django


# Let Django apps accessible through sys.path
_this_filepath = Path(os.path.realpath(__file__))
_apps_dirpath = _this_filepath.parent.parent.parent
sys.path.insert(0, str(_apps_dirpath))

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
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
]

# extensions dedicated configuration:
# - sphinx.ext.todo:
todo_include_todos = True

templates_path = ['_templates']
exclude_patterns = []

language = 'fr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'library'
html_static_path = ['_static']
html_copy_source = False

