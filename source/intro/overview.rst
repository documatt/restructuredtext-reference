##################
|rst| overview
##################

If you starting writing in |rst|, you will find it's not always intuitive. In this guide, you'll find explanation in plain English of syntax, elementary concepts and important pitfalls to avoid.

What is |rst|?
**************

|rst| is a lightweight markup language for writing articles, blog posts, documents, and books.

Its syntax (the rules of writing) is suited for a documentation. Programmers write in Java, Python, etc., while tech writers write in plain text files containing |rst|. It has a syntax very similar to its close relative Markdown.

Documentation languages as |rst| are also called *markup* languages, because they add the formatting and semantic meaning to the plain text. At the time of writing, you should not be concerned how the text will look like at production. The outputs like web page or PDF may look very different. You concentrate on the structure and content at writing time, not the visual appearance.

For brevity, it is often abbreviated as RST or reST (don't confuse with the REST which is kind of APIs). A file extension is often ``.rst`` or ``.txt``.

Sample document
***************

Have look at the following example of document written using |rst|.

.. datatemplate:yaml:: /_data/snippet/rst-sample-document.yaml
   :template: snippet-new-window.rst.jinja

.. _syntax-block-vs-inline:

.. include:: /inc/block-vs-inline.rst

Whitespace and indentation
**************************

Whitespaces
===========

Whitespaces are invisible but very important characters not only in |rst|. The common whitespaces are under the :kbd:`Space` and :kbd:`Tab` keys.

Blank lines
===========

Blank lines are important. For example, they separate :doc:`/element/paragraph/` and other block elements, or delimit sublist within a list.

.. datatemplate:yaml:: /_data/snippet/rst-blank-lines1.yaml
   :template: snippet.rst.jinja

In normal text, multiple successive blank lines are considered as a single blank line. They are only preserved in the :doc:`literal blocks </element/literal-block>`.

.. datatemplate:yaml:: /_data/snippet/rst-blank-lines2.yaml
   :template: snippet.rst.jinja

Indentation
===========

Tricky part of |rst| is indentation. Indentation means putting whitespaces before the line text itself. We strongly recommend you to use space characters (via :kbd:`Space` key) instead of tabs (via :kbd:`Tab` key).

.. caution:: Keeping proper indentation and blank line separators in |rst| is definitively the biggest trouble not only for beginners! Read the following part very carefully.

The indentation is part of the syntax of many |rst| elements:

* block quotes
* definition lists
* bullet and enumerated lists
* content of literal blocks
* content of blocks like directive, footnote, comment, etc.
* any nested content, e.g. a list withing another list item

Wrongly indented means wrongly recognized. For example, just indenting the second paragraph makes it the block quote element. First and third has original indentation and thus are normal paragraphs.

.. datatemplate:yaml:: /_data/snippet/rst-indentation1.yaml
   :template: snippet.rst.jinja

Comments
********

Comments are parts of text that should be processed. Syntax is :literal:`\.\.\ ` (two dots and one space).

::

    .. This is a comment.

For multline commends you need to indent the text after :literal:`\.\.\ `:

::

    ..
       This whole indented block
       is a comment.

       Still in the comment.


Inline comments are not supported. For example, JavaScript supports inline comments with ``/*`` and ``*/``, e.g. ``let foo = /* inline comment */ 'bar';``.