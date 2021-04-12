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

project = 'reStructuredText and Sphinx Reference'
copyright = '2020, Matt from Documatt'
author = 'Matt from Documatt'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinxcontrib.datatemplates',
    'sphinx_sitemap'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'README.rst']

highlight_language = 'none'

rst_epilog = '''
.. |rst| replace:: reStructuredText
'''


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# html_theme = "learn_basic"

html_theme = "sphinx_documatt_theme"

html_logo = '../logo.svg'

html_theme_options = {
    'motto': 'Example based gentle reference of the reStructuredText and <a href="https://www.sphinx-doc.org">Sphinx</a> syntax, directives, roles and common issues. It demonstrates almost all the markup making it also good for testing Sphinx themes. Free and <a href="https://gitlab.com/documatt/sphinx-reference-project">open-source</a>.',
    'header_logo_style': 'width: 4rem;',
    'footer_logo_style': 'width: 4rem;',
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = ['custom.css']

# Additional templates that should be rendered to pages, maps page names to
# template names.
html_additional_pages = {
    'index': 'index.html',
}

# Enables sectionauthor and codeauthor roles
show_authors = True

# Don't copy sources, hide "Show Source"
html_copy_source = False
html_show_sourcelink = False


# A list of paths that contain extra files not directly related to the documentation, such as
# robots.txt or .htaccess. Relative paths are taken as relative to the configuration directory.
# They are copied to the output directory. They will overwrite any existing file of the same name.
# As these files are not meant to be built, they are automatically excluded from source files.
html_extra_path = ['_extra', 'robots.txt']

html_codeblock_linenos_style = 'inline'