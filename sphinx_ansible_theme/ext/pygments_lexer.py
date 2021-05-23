"""Sphinx extension setting up an 'ansible-output' lexer."""
from sphinx_ansible_theme._pygments.lexer import AnsibleOutputLexer


__version__ = "0.1.0"
__license__ = "BSD license"
__author__ = "Felix Fontein"
__author_email__ = "felix@fontein.de"


def setup(app):
    """Initialize Sphinx extension API.

    See http://www.sphinx-doc.org/en/stable/extdev/index.html#dev-extensions.
    """
    lexer = AnsibleOutputLexer(startinline=True)
    for alias in (lexer.name, *lexer.aliases):
        app.add_lexer(alias, lexer)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
