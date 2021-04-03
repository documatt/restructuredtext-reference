################################################################################
Images
################################################################################

.. sidebar:: Image elements

   .. datatemplate:yaml:: /_data/collection/images.yaml
      :template: collection.rst.jinja

A picture is worth a thousand words. Generally, pictures in documentation serve two purposes – they are a complement to the text or replace the textual description. Some people learn better with words, others with pictures (or videos).

In documentation, we recognize *screenshots* which are pictures of a computer screen, or schematic *drawings* as various diagrams and charts (UML, ERD, flowcharts, ...).

Other names for picture are *image* and *figure*. Generally, you can use all three interchangeably. However, in |rst|, :doc:`/element/image` element is a simple picture, while :doc:`/element/figure` element has a caption, can be numbered, hyperlinked from the text, and is generally suitable for more formal books.

.. image:: /img/image-vs-figure.png
   :width: 75%

Third type of picture, :doc:`/element/inline-image`, is just as a regular image but placed inside a line text and behaves as a :doc:`inline element <inline-elements>`.

.. image:: /img/inline-image.png
   :width: 37.5%