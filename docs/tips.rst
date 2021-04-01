###############
Tips and tricks
###############

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
**************

::
    
    $ datatemplate render source/_templates/element.rst.jinja source/_data/element/inline-literal.yaml > test.rst