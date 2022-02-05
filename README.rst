sphinx_ansible_theme
--------------------

A reusable Ansible Sphinx Theme.

Demo-site at https://sphinx-ansible-theme.readthedocs.io/en/latest/

Logos in ``sphinx_ansible_theme/static/images/``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Ansible logos are taken from `the official Ansible Community logo download page <https://www.ansible.com/logos>`_. The files are slightly modified as follows:

* The SVG logos' bounding boxes are modified from ``0 0 300 300`` to ``30 30 240 240``.
* The PNG files are rescaled to 180x180 using ImageMagick as follows:

  .. code-block:: sh

    convert Ansible-Mark-Large-RGB-Black.png -resize 180x180 Ansible-Mark-RGB_Black.png
    convert Ansible-Mark-Large-RGB-White.png -resize 180x180 Ansible-Mark-RGB_White.png
