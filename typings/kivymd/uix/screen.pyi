"""
This type stub file was generated by pyright.
"""

from kivy.uix.screenmanager import Screen
from kivymd.uix import MDAdaptiveWidget
from kivymd.uix.behaviors import DeclarativeBehavior
from kivymd.uix.hero import MDHeroTo

"""
Components/Screen
=================

:class:`~kivy.uix.screenmanager.Screen` class equivalent. Simplifies working
with some widget properties. For example:

Screen
------

.. code-block:: kv

    Screen:
        canvas:
            Color:
                rgba: app.theme_cls.primary_color
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [25, 0, 0, 0]

MDScreen
--------

.. code-block:: kv

    MDScreen:
        radius: [25, 0, 0, 0]
        md_bg_color: app.theme_cls.primary_color
"""
class MDScreen(DeclarativeBehavior, Screen, MDAdaptiveWidget):
    """
    Screen is an element intended to be used with a
    :class:`~kivymd.uix.screenmanager.MDScreenManager`. For more information,
    see in the :class:`~kivy.uix.screenmanager.Screen` class documentation.
    """
    hero_to = ...
    heroes_to = ...
    def on_hero_to(self, screen, widget: MDHeroTo) -> None:
        """Called when the value of the :attr:`hero_to` attribute changes."""
        ...
    


