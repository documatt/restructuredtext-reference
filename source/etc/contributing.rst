############
Contributing
############

Did you find a typo or bad information? Help by contributing to this project. Fork our `GitLab repository <https://gitlab.com/documatt/sphinx-reference-project>`_ and propose improvement in merge request, or file an issue. On this page, you will find how is project files organized.

**********************
On-disk file structure
**********************

::

   originals/ - diagrams and illustration source files (.afdesign)
   source/
       _data/ - descriptions (actual content)
           collection/ - YAMLs describing collections
           element/ - YAMLs descripting elements
           snippets/ - YAMLs describing snippets
       _static/ - theme overrides
       _templates/ - sphinxcontrib.datatemplates' templates (.rst.jinja),
                     Sphinx Theme templates (.html), and
                     description YAML templates (.yaml.jinja)
       element/ - RST skeletons for elements
       example/ - RST examples that must be open in the
                  the separate page (e.g., examples of sections)
   index.rst - master doc
   *.rst - RST collection skeletons

Project uses `Sphinx documentation <https://www.sphinx-doc.org/>`_ and amazing `sphinxcontrib.datatemplates extension <https://pypi.org/project/sphinxcontrib.datatemplates/>`_.

Sphinx Reference knows only two types of descriptions:

* a Sphinx element
* a collection of Sphinx elements

Website is generated from YAML data files and Jinja templates creating RST files. Thanks to Jinja templates, all pages for the same type looks the same.

.. important:: Data files are expected to have ``.yaml`` extension. ``.yml`` will cause error.

Skeleton contains no or minimal real content (e.g. only a introduction to a topic). Their purpose is to glue actual descriptions from YAMLs in ``_data/`` into sphinxcontrib.datatemplates' templates in ``_templates/``.

********
Elements
********

Element on the disk comprises:

* data ``_data/element/<element-name>.yaml`` with the content described bellow
* skeleton ``elements/<element-name>.rst`` with content::

    .. datatemplate:yaml:: /_data/element/<element-name>.yaml
       :template: element.rst.jinja

YAML schema for element:

* ``title``
* ``desc``
* ``collections`` - element belogs to these collections
* ``url``
* list of ``examples`` where each contain attributes:

  * ``name``
  * ``desc``
  * ``source``

Example:

.. literalinclude:: /_data/element/hint.yaml

How to add element
==================

#. Create element description ``_data/element/<element-name>.yaml``. Template is at ``_templates/element.yaml.jinja``.
#. Add element to ``collections`` attribute in YAML. Items are filenames (without suffix) from ``source/_data/_collection``.
#. Add element to list in ``_data/collection/<collection-name>.yaml``. Items are filenames (without suffix) of element skeleton.
#. Create element skeleton ``element/<element-name>.yaml``. Template is at ``_templates/element-skeleton.rst.jinja``.

***********
Collections
***********

Collection on the disk comprises:

* data ``_data/collection/<collection-name>.yaml`` with list of elements. Names in the list must exactly correspond to filenames in ``_data/element/<element>.yaml``. E.g.::

    elements:
      - attention
      - caution
      - danger
      - error
      - hint
      - important
      - note
      - tip
      - warning
      - admonition
      - seealso

* skeleton ``<collection-name>.rst`` with content::

    .. datatemplate:json:: /_data/element/<collection-name>.yaml
       :template: collection.rst.jinja

How to add collection
=====================

#. Create collection description ``_data/collection/<collection-name>.yaml``. Template is at ``_templates/collection.yaml.jinja``. Content are elements belonging to it.
#. Create element skeleton ``<collection-name>.rst``. Template is at ``_templates/collection-skeleton.rst.jinja``.
#. Add element skeleton to toctree in master document ``index.rst``.

***************
Tips and tricks
***************

Dump variable
=============

If you want to see that is actually in the variable, print it as ``<pre>``. E.g.::

    .. raw:: html

       <pre>{{ example.rst }}</pre>

Or, repeat full problematic part::

    .. raw:: html

       <pre>
       {% for line in example.rst %}
       {{ line }}
       {% endfor %}
       </pre>

Render to file
==============

Useful for templates debugging.

::

    $ datatemplate render source/_templates/element.rst.jinja source/_data/element/inline-literal.yaml > test.rst