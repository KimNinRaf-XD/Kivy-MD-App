"""
This type stub file was generated by pyright.
"""

from kivy.uix.layout import Layout

'''
Anchor Layout
=============

.. only:: html

    .. image:: images/anchorlayout.gif
        :align: right

.. only:: latex

    .. image:: images/anchorlayout.png
        :align: right

The :class:`AnchorLayout` aligns its children to a border (top, bottom,
left, right) or center.


To draw a button in the lower-right corner::

    layout = AnchorLayout(
        anchor_x='right', anchor_y='bottom')
    btn = Button(text='Hello World')
    layout.add_widget(btn)

'''
__all__ = ('AnchorLayout', )
class AnchorLayout(Layout):
    '''Anchor layout class. See the module documentation for more information.
    '''
    padding = ...
    anchor_x = ...
    anchor_y = ...
    def __init__(self, **kwargs) -> None:
        ...
    
    def do_layout(self, *largs): # -> None:
        ...
    

