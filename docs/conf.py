# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys
import os

sys.path.insert(0, os.path.abspath("../"))

from xionfunctions import __version__

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'xionfunctions'
copyright = '2024, XENO'
author = 'XENO'
release = __version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
    "sphinx_autodoc_typehints",
    "myst_parser"
]

intersphinx_mapping = {
    "py": ("https://docs.python.org/3", None),
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'  # Furo theme is modern and includes a sidebar TOC by default
html_static_path = ['_static']

# Options for Furo theme
html_theme_options = {
    "navigation_depth": 2,  # Adjust the depth of the navigation tree
    "sidebar_hide_name": True,  # Hide the project name from the sidebar (optional)
}

# If you have any custom static files, you can add them to the `_static` directory.
