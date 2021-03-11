# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('./_extensions'))

# -- Project information -----------------------------------------------------

project = 'Sphinx Demo Project'
copyright = '2020, Matt from Documatt'
author = 'Matt from Documatt'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx_tabs.tabs',
    'sphinxcontrib.datatemplates'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'README.rst']

# rst_epilog = f'''
# .. |project| replace:: {project}
# '''


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# html_theme = "learn_basic"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# Enables sectionauthor and codeauthor roles
show_authors = True

# -- Options for jinja extension ----------------------------------------------

jinja_contexts = {
    'first_ctx': {'topics': {'a': 'b', 'c': 'd'}},
    'second_ctx': {'topics': {'a': 'b', 'c': 'd'}},
    'third_ctx': {'objects': [
        [1, 2, 3, 4],
        'skipped_string',
        ['a', 'b'],
    ]},
}
