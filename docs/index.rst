Sphinx Ansible Theme
====================

This theme is building on top of RTD Theme and adds customizations needed
for building projects which are part of Ansible ecosystem.


.. code-block:: yaml

    a_list:
      - name: foo
        image: bar
        # …

::

    # this code block should used default lexer
    - hosts: all
      tasks:
        - debug:
            msg: "oops!"
