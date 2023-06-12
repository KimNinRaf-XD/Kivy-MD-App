"""
This type stub file was generated by pyright.
"""

from kivy.effects.scroll import ScrollEffect

'''
Damped scroll effect
====================

.. versionadded:: 1.7.0

This damped scroll effect will use the
:attr:`~kivy.effects.scroll.ScrollEffect.overscroll` to calculate the scroll
value, and slows going back to the upper or lower limit.

'''
__all__ = ('DampedScrollEffect', )
class DampedScrollEffect(ScrollEffect):
    '''DampedScrollEffect class. See the module documentation for more
    information.
    '''
    edge_damping = ...
    spring_constant = ...
    min_overscroll = ...
    round_value = ...
    def update_velocity(self, dt): # -> None:
        ...
    
    def on_value(self, *args): # -> None:
        ...
    
    def on_overscroll(self, *args): # -> None:
        ...
    
    def apply_distance(self, distance): # -> None:
        ...
    

