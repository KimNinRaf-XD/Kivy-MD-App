"""
This type stub file was generated by pyright.
"""

'''
Parser utilities
================

Helper functions used for CSS parsing.
'''
__all__ = ('parse_color', 'parse_int', 'parse_float', 'parse_string', 'parse_bool', 'parse_int2', 'parse_float4', 'parse_filename')
class ColorException(Exception):
    ...


def parse_filename(filename): # -> str:
    '''Parse a filename and search for it using `resource_find()`.
    If found, the resource path is returned, otherwise return the unmodified
    filename (as specified by the caller).'''
    ...

def color_error(text): # -> tuple[Literal[0], Literal[0], Literal[0], Literal[1]]:
    ...

def parse_color(text): # -> tuple[Literal[0], Literal[0], Literal[0], Literal[1]] | list[float | int] | list[float] | list[int]:
    '''Parse a string to a kivy color. Supported formats:

        * rgb(r, g, b)
        * rgba(r, g, b, a)
        * rgb
        * rgba
        * rrggbb
        * rrggbbaa

    For hexadecimal values, you case also use:

        * #rgb
        * #rgba
        * #rrggbb
        * #rrggbbaa
    '''
    ...

def parse_bool(text): # -> bool:
    '''Parse a string to a boolean, ignoring case. "true"/"1" is True,
    "false"/"0" is False. Anything else throws an exception.'''
    ...

def parse_string(text):
    '''Parse a string to a string (removing single and double quotes).'''
    ...

def parse_int2(text): # -> list[parse_int]:
    '''Parse a string to a list of exactly 2 integers.

        >>> print(parse_int2("12 54"))
        12, 54

    '''
    ...

def parse_float4(text): # -> list[parse_float]:
    '''Parse a string to a list of exactly 4 floats.

        >>> parse_float4('54 87. 35 0')
        54, 87., 35, 0

    '''
    ...

parse_int = int
parse_float = float