"""
This type stub file was generated by pyright.
"""

from kivy.utils import platform

'''
Resources management
====================

Resource management can be a pain if you have multiple paths and projects.
Kivy offers 2 functions for searching for specific resources across a list
of paths.

Resource lookup
---------------

When Kivy looks for a resource e.g. an image or a kv file, it searches through
a predetermined set of folders. You can modify this folder list using the
:meth:`resource_add_path` and :meth:`resource_remove_path` functions.

Customizing Kivy
----------------

These functions can also be helpful if you want to replace standard Kivy
resources with your own. For example, if you wish to customize or re-style
Kivy, you can force your *style.kv* or *data/defaulttheme-0.png* files to be
used in preference to the defaults simply by adding the path to your preferred
alternatives via the :meth:`resource_add_path` method.

As almost all Kivy resources are looked up using the :meth:`resource_find`, so
you can use this approach to add fonts and keyboard layouts and to replace
images and icons.

'''
__all__ = ('resource_find', 'resource_add_path', 'resource_remove_path')
resource_paths = ...
if platform == 'ios':
    ...
def resource_find(filename, use_cache=...): # -> str | None:
    '''Search for a resource in the list of paths.
    Use resource_add_path to add a custom path to the search.
    By default, results are cached for 60 seconds.
    This can be disabled using use_cache=False.

    .. versionchanged:: 2.1.0
        `use_cache` parameter added and made True by default.
    '''
    ...

def resource_add_path(path): # -> None:
    '''Add a custom path to search in.
    '''
    ...

def resource_remove_path(path): # -> None:
    '''Remove a search path.

    .. versionadded:: 1.0.8
    '''
    ...

