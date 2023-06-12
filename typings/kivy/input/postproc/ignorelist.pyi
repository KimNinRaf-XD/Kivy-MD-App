"""
This type stub file was generated by pyright.
"""

'''
Ignore list
===========

Ignore touch on some areas of the screen
'''
__all__ = ('InputPostprocIgnoreList', )
class InputPostprocIgnoreList:
    '''
    InputPostprocIgnoreList is a post-processor which removes touches in the
    Ignore list. The Ignore list can be configured in the Kivy config file::

        [postproc]
        # Format: [(xmin, ymin, xmax, ymax), ...]
        ignore = [(0.1, 0.1, 0.15, 0.15)]

    The Ignore list coordinates are in the range 0-1, not in screen pixels.
    '''
    def __init__(self) -> None:
        ...
    
    def collide_ignore(self, touch): # -> Literal[True] | None:
        ...
    
    def process(self, events): # -> list[tuple[Unknown, Unknown]]:
        ...
    

