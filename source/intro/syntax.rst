############
|rst| syntax
############

.. _syntax-block-vs-inline:

.. include:: /inc/block-vs-inline.rst


Blank lines
===========

Blank lines are important. For example, they create :doc:`/element/paragraph/`.

Paragraphs
**********

* shortened to "para" and corresponds to ``<p>`` HTML tag
* are basic processing "units", e.g. for translattion
* paragraph is created by blank line
* do long single-lined paras (easier diffs in Git)

::

    this is the
    first paragraph

    second paragraph


US-ASCII characters
*******************

Backtick:
-

Single quote:

- not "If you don’t want any highlighting, use none or text."

Double quote:

- not It's not “autodetect” or “none”

Hyphen:

- any language you might imagine – just use python, java

Tři tečky (ellipsis):

- python, java, javascript, c++, html, json, … as a code-block argument