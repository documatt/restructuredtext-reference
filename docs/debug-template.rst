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
