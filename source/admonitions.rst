################################################################################
Admonitions
################################################################################

.. sidebar:: Admonition elements

   .. datatemplate:yaml:: /_data/collection/admonitions.yaml
      :template: collection.rst.jinja

Admonitions are visually bold blocks like "tip", "note", "important". They can appear anywhere an ordinary body element can. Readers will appreciate if you spice up your text with admonitions like tip for extra information or warning to raise their attention.

Specific or generic?
********************

|rst| contains one :doc:`generic </element/admonition>` and ten specific admonitions: :doc:`/element/attention`, :doc:`/element/caution`, :doc:`/element/danger`, :doc:`/element/error`, :doc:`/element/hint`, :doc:`/element/important`, :doc:`/element/note`, :doc:`/element/tip`, :doc:`/element/warning`, and :doc:`/element/seealso`.

Specific admonitions are often rendered in colors according to their severity. Their title is their name and can't be changed.

.. datatemplate:yaml:: /_data/snippet/admonitions1.yaml
   :template: snippet.rst.jinja

Generic admonition has a title and usually neutral appearance.

.. datatemplate:yaml:: /_data/snippet/admonitions2.yaml
   :template: snippet.rst.jinja

Admonitions in uppercase
************************

Admonition directives are case insensitive (like all directive and role names). Most documentation and book authors prefer typing directives and roles all in lowercase.

.. code-block:: rst
   :linenos:

   .. important:: Most reStructuredText authors write directives like note in lowercase

However, writing admonitions directive in uppercase corresponds with their “raise attention” objective.

.. code-block:: rst
   :linenos:

   .. IMPORTANT:: However writing admonitions uppercase can be considered as reasonable exception to "everything-lowercase" rule.

Complex admonition
******************

Any |rst| elements can be in admonition content. As always, you need only to keep correct indentation.

.. datatemplate:yaml:: /_data/snippet/admonitions2.yaml
   :template: snippet.rst.jinja

Content on the same line, or bellow
***********************************

You can't type specific admonition incorrectly. They accept its text in on the same line, bellow (optionally separated by a blank line), or on both places (strings are concatenated).

.. danger:: On the opposite, :doc:`generic admonition has very strict syntax </element/admonition>`.

The following specific admonition markups are all valid. For example, attention admonition:

.. code-block:: rst
   :linenos:

   .. attention:: I'm attention text on the same line

..

.. code-block:: rst
   :linenos:

   .. attention::
      I'm attention text on the line bellow

..

.. code-block:: rst
   :linenos:

   .. attention::
      
      I'm attention text bellow separated by the blank line

..

.. code-block:: rst
   :linenos:

   .. attention:: I'm attention text
      that continues bellow

..

.. code-block:: rst
   :linenos:

   .. attention:: I'm attention text

      that continues bellow after the blank line