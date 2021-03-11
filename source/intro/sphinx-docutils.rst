####################
Sphinx and Docutils
####################

Sphinx and Docutils are two crutial and interconnected tools for technical writing in |rst|.

Sphinx
******

Sphinx (https://www.sphinx-doc.org/) is a tool that takes reStructuredText files and build a documentation in formats like HTML or PDF. Sphinx is not the only tool that works with the |rst|, but is the most advanced and the most used in the industry.

Sphinx also adds few new useful constructs to the |rst|, e.g. for creating a table of contents, documenting programming language code. |rst| and Sphinx makes a perfect couple.

Sphinx is command-line tool with no graphical interface. Write ``.rst`` files in any (plain) text editor you like. Folder with ``.rst`` files and Sphinx configuration file ``conf.py`` is called *Sphinx project*.

To invoke Sphinx to build a project, do e.g. (on the Linux or macOS)::

    $ cd my_sphinx_project

    $ ls
    conf.py
    index.rst
    overview.rst
    pitfalls.rst

    $ make html

and Sphinx will produce HTML version of the project.

Docutils
********

Sphinx is build upon Docutils (https://docutils.sourceforge.io) to parse and write documents in |rst| text.
