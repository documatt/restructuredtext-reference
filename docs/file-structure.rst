######################
On-disk file structure
######################

Sphinx Reference knows only two types of items: Sphinx element and collections of Sphinx elemenets.

Website is generated from YAML data files and Jinja templates creating RST files. Thanks to Jinja templates, all pages for the same type looks the same.

.. important:: Data files are expected to have ``.yaml`` extension. ``.yml`` will cause error.

Elements
********

Element on the disk comprises:

* data ``_data/element/<element-name>.json`` in :ref:`expected format <element-schema>`
* document ``elements/<element-name>.rst`` with content::

    .. datatemplate:json:: /_data/element/<element-name>.json
       :template: element.rst.jinja

All elements have identical page thanks to ``_/templates/element.rst.jinja``.

Collections
***********

Collection on the disk comprises:

* data ``_data/element/<collection-name>.json`` in :ref:`expected format <collection-schema>`
* document ``collection/<collection-name>.rst`` with content::

    .. datatemplate:json:: /_data/element/<collection-name>.json
       :template: collection.rst.jinja

All collections have identical page thanks to ``_/templates/collection.rst.jinja``.
