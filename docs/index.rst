Sphinx Ansible Theme
====================

This theme is building on top of RTD Theme and adds customizations needed
for building projects which are part of Ansible ecosystem.


.. code-block:: yaml

    a_list:
      - name: foo
        image: bar
    # Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

::

    # this code block should used default lexer
    - hosts: all
      tasks:
        - debug:
            msg: "oops!"
