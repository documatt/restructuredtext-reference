################################################################################
Lists
################################################################################

.. sidebar:: Elements

   .. datatemplate:yaml:: /_data/collection/lists.yaml
      :template: collection.rst.jinja

List items indentation
**********************

Tricky part of reStructuredText is indentation. Wrongly indented means wrongly recognized.

Extreme attention has to be paid for bullet or enumerated lists. List item content needs to keep proper indentation level.

.. datatemplate:yaml:: /_data/snippet/list1.yaml
   :template: snippet.rst.jinja

Sublists indentation
*********************

Another source of pain is keeping proper indentation when creating nested lists (sublists).

.. datatemplate:yaml:: /_data/snippet/sublist1.yaml
   :template: snippet.rst.jinja

Previous example also shows that block elements must be separated by the at least one blank line. If you forgot to separate sublist new a blank line, it will be a continuation of item #1:

.. datatemplate:yaml:: /_data/snippet/sublist2.yaml
   :template: snippet.rst.jinja

Another crazy situation easily occurs if you indent the sublist, but not at the same level as the parent item:

.. datatemplate:yaml:: /_data/snippet/sublist3.yaml
   :template: snippet.rst.jinja