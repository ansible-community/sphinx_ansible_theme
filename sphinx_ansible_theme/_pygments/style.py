from pygments.style import Style
from pygments.token import (
    Keyword,
    Name,
    Comment,
    Error,
    Number,
    Operator,
    Generic,
    Whitespace,
    Punctuation,
    Literal,
)


class AnsibleStyle(Style):
    """Ansible's GitHub-like highlighting."""

    background_color = "#f8f8f8"  # class: '.highlight'
    highlight_color = "#ffffcc; border: 1px solid #edff00; padding-top: 2px; border-radius: 3px; display: block"
    default_style = ""

    styles = {
        Error: "#a61717 bg:#e3d2d2 border:#FF0000",  # class: 'err'
        # Error:                     "#a61717 bg:#e3d2d2 border:1px solid #FF0000", # class: 'err'
        Comment: "italic #6a737d",  # class: 'c'
        Comment.Preproc: "noitalic #007020",  # class: 'cp'
        Comment.PreprocFile: "italic #6a737d",  # class: 'cpf'
        Comment.Hashbang: "italic #6a737d",  # class: 'ch'
        Comment.Multiline: "italic #6a737d",  # class: 'cm'
        Comment.Single: "italic #6a737d",  # class: 'c1'
        Comment.Special: "bold italic #999999 bg:#fff0f0",  # class: 'cs'
        Keyword: "bold #007020",  # class: 'k'
        Keyword.Constant: "bold #007020",  # class: 'kc'
        Keyword.Declaration: "bold #007020",  # class: 'kd'
        Keyword.Namespace: "bold #007020",  # class: 'kn'
        Keyword.Pseudo: "#007020",  # class: 'kp'
        Keyword.Reserved: "bold #007020",  # class: 'kr'
        Keyword.Type: "#902000",  # class: 'kt'
        Operator: "bold #666666",  # class: 'o'
        Operator.Word: "bold #007020",  # class: 'ow'
        # FIXME: Indicator?
        Punctuation: "bold",  # class: 'p'
        Name: "#333333",  # class: 'n'
        Name.Attribute: "#008080",  # class: 'na'
        Name.Builtin: "#0086b3",  # class: 'nb'
        Name.Class: "bold #445588",  # class: 'nc'
        Name.Constant: "#008080",  # class: 'no'
        Name.Decorator: "bold #555555",  # class: 'nd'
        Name.Entity: "bold #800080",  # class: 'ni'
        Name.Exception: "bold #990000",  # class: 'ne'
        Name.Function: "bold #990000",  # class: 'nf'
        Name.Label: "bold #002070",  # class: 'nl'
        Name.Namespace: "bold #555555",  # class: 'nn'
        Name.Tag: "bold #22863a",  # class: 'nt'
        Name.Variable: "bold #9960b5",  # class: 'nv'
        Name.Builtin.Pseudo: "#999999",  # class: 'bp'
        Name.Function.Magic: "#06287e",  # class: 'fm'
        Name.Variable.Class: "#008080",  # class: 'vc'
        Name.Variable.Global: "#008080",  # class: 'vg'
        Name.Variable.Instance: "#008080",  # class: 'vi'
        Name.Variable.Magic: "#bb60d5",  # class: 'vm'
        # FIXME: Literal.Number?
        Number: "#208050",  # class: 'm'
        Literal: "#032f62",  # class: 'l'
        Literal.String: "#4070a0",  # class: 's'
        Literal.Number.Bin: "#009999",  # class: 'mb'
        Literal.Number.Float: "#009999",  # class: 'mf'
        Literal.Number.Hex: "#009999",  # class: 'mh'
        Literal.Number.Integer: "#009999",  # class: 'mi'
        Literal.Number.Oct: "#009999",  # class: 'mo'
        Literal.String.Affix: "#dd1144",  # class: 'sa'
        Literal.String.Backtick: "#dd1144",  # class: 'sb'
        Literal.String.Char: "#dd1144",  # class: 'sc'
        Literal.String.Delimiter: "#dd1144",  # class: 'dl'
        Literal.String.Doc: "italic #dd1144",  # class: 'sd'
        Literal.String.Double: "#dd1144",  # class: 's2'
        Literal.String.Escape: "bold #dd1144",  # class: 'se'
        Literal.String.Heredoc: "#dd1144",  # class: 'sh'
        Literal.String.Interpol: "italic #dd1144",  # class: 'si'
        Literal.String.Other: "#dd1144",  # class: 'sx'
        Literal.String.Regex: "#009926",  # class: 'sr'
        Literal.String.Single: "#dd1144",  # class: 's1'
        Literal.String.Symbol: "#990073",  # class: 'ss'
        Literal.Number.Integer.Long: "#009999",  # class: 'il'
        Generic.Deleted: "#A00000 bg:#ffdddd",  # class: 'gd'
        Generic.Emph: "italic",  # class: 'ge'
        Generic.Error: "#aa0000",  # class: 'gr'
        Generic.Heading: "bold #000080",  # class: 'gh'
        Generic.Inserted: "#00A000 bg:#ddffdd",  # class: 'gi'
        Generic.Output: "#333333",  # class: 'go'
        Generic.Prompt: "bold #c65d09",  # class: 'gp'
        Generic.Strong: "bold",  # class: 'gs'
        Generic.Subheading: "bold #800080",  # class: 'gu'
        Generic.Traceback: "#0040D0",  # class: 'gt'
        Whitespace: "#bbbbbb",  # class: 'w'
    }
