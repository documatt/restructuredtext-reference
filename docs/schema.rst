############
JSON schemas
############

ELement
*******


Collections
***********

Stored in ``_data/collection``. E.g.::

    {
      "title": "Admonitions",
      "desc": "Are this and that...",
      "elements": [
        "attention"
      ]
    }

where

* ``title`` page title
* ``desc`` description bellow title
* ``elements`` list element name that belongs this collection. The name must exactly correspond to the ``_data/element/<element>.json`` that will be included into the page.
