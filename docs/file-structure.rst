######################
On-disk file structure
######################

Folders and files
*****************

::

    docs/ - these docs
    source/
        _data/ - descriptions
            collection/ - YAMLs describing collections
            element/ - YAMLs descripting elements
            snippets/ - YAMLs describing snippets
        _static/ - theme overrides
        element/ - RST skeletons for elements
        example/ - RST fragments that must be displayed on
                   the separate page (e.g., examples of sections)
    index.rst - master docs
    *.rst - RST collection skeletons

Descriptions
************

Sphinx Reference knows only two types of items: Sphinx element and collections of Sphinx elemenets.

Website is generated from YAML data files and Jinja templates creating RST files. Thanks to Jinja templates, all pages for the same type looks the same.

.. important:: Data files are expected to have ``.yaml`` extension. ``.yml`` will cause error.

Elements
========

Element on the disk comprises:

* data ``_data/element/<element-name>.yaml`` in :ref:`expected format <element-schema>`
* document ``elements/<element-name>.rst`` with content::

    .. datatemplate:yaml:: /_data/element/<element-name>.yaml
       :template: element.rst.jinja

All elements have identical page thanks to Jinja template.

Collections
===========

Collection on the disk comprises:

* data ``_data/element/<collection-name>.json`` in :ref:`expected format <collection-schema>`
* document ``collection/<collection-name>.rst`` with content::

    .. datatemplate:json:: /_data/element/<collection-name>.json
       :template: collection.rst.jinja

All collections have identical page thanks to Jinja template.
