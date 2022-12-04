# -*- coding: utf-8 -*-
"""Documentation Configuration."""

# pip install sphinx_ansible_theme
from sphinx_ansible_theme import __version__


VERSION = __version__
AUTHOR = 'Ansible Community'


# General configuration
# ---------------------

extensions = [
    'sphinx.ext.autodoc',
    'notfound.extension',
]

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
root_doc = master_doc = 'index'  # Sphinx 4+ / 3-

# General substitutions.
project = 'Sphinx Ansible Theme'
copyright = f'2020 {AUTHOR}'

# The default replacements for |version| and |release|, also used in various
# other places throughout the built documents.
#
# The short X.Y version.
version = '.'.join(VERSION.split('.')[:2])
# The full version, including alpha/beta/rc tags.
release = VERSION

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = '%B %d, %Y'

# The reST default role (used for this markup: `text`) to use for all
# documents.
default_role = 'any'

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
show_authors = True

# The name of the Pygments (syntax highlighting) style to use.
# pygments_style = 'sphinx'
pygments_style = 'ansible'

highlight_language = 'YAML+Jinja'

# Substitutions, variables, entities, & shortcuts for text which do not need to link to anything.
# For titles which should be a link, use the intersphinx anchors set at the index, chapter, and section levels, such as  qi_start_:
# |br| is useful for formatting fields inside of tables
# |_| is a nonbreaking space; similarly useful inside of tables
rst_epilog = """
.. |br| raw:: html

   <br>
.. |_| unicode:: 0xA0
    :trim:
"""


# Options for HTML output
# -----------------------

html_theme = 'sphinx_ansible_theme'
html_show_sphinx = True

html_theme_options = {
    # 'canonical_url': "https://docs.ansible.com/ansible/latest/",
    'vcs_pageview_mode': 'edit',
    'topbar_links': {
        'AnsibleFest': 'https://www.ansible.com/ansiblefest',
        'Products': 'https://www.ansible.com/tower',
        'Community': 'https://www.ansible.com/community',
        'Webinars & Training': 'https://www.ansible.com/webinars-training',
        'Blog': 'https://www.ansible.com/blog',
    },
    # URL to send the user to when clicking on the title link
    'documentation_home_url': '/',
}

html_context = {
    'display_github': 'True',
    'github_user': 'ansible-community',
    'github_repo': 'sphinx_ansible_theme',
    'github_version': 'devel/docs/docsite/rst/',
    'github_module_version': 'devel/lib/ansible/modules/',
    'github_root_dir': 'devel/lib/ansible',
    'github_cli_version': 'devel/lib/ansible/cli/',
    'current_version': version,
    'latest_version': 'latest',
    # list specifically out of order to make latest work
    'available_versions': ('latest', ),
}

# Add extra CSS styles to the resulting HTML pages
html_css_files = [
    'css/color-scheme.css',
]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = f'{project} Documentation'

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = 'Documentation'

# The name of an image file (within the static path) to place at the top of
# the sidebar.
html_logo = '_static/images/logo_invert.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = '_static/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, the reST sources are included in the HTML build as _sources/<name>.
html_copy_source = False

# Configuration for sphinx-notfound-pages
# with no 'notfound_template' and no 'notfound_context' set,
# the extension builds 404.rst into a location-agnostic 404 page
#
# default is `en`:
notfound_default_language = "en"
# default is `latest`:
notfound_default_version = "latest"
# makes default setting explicit:
notfound_no_urls_prefix = False
