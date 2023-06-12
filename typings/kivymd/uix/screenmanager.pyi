"""
This type stub file was generated by pyright.
"""

from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.behaviors import DeclarativeBehavior

"""
Components/ScreenManager
========================

.. versionadded:: 1.0.0

:class:`~kivy.uix.screenmanager.ScreenManager` class equivalent.
If you want to use Hero animations you need to use
:class:`~kivymd.uix.screenmanager.MDScreenManager` not
:class:`~kivy.uix.screenmanager.ScreenManager` class.

Transition
----------

:class:`~kivymd.uix.screenmanager.MDScreenManager` class supports the following
transitions:

- :class:`~kivymd.uix.transition.MDFadeSlideTransition`
- :class:`~kivymd.uix.transition.MDSlideTransition`
- :class:`~kivymd.uix.transition.MDSwapTransition`

You need to use the :class:`~kivymd.uix.screenmanager.MDScreenManager` class
when you want to use hero animations on your screens. If you don't need hero
animation use the :class:`~kivy.uix.screenmanager.ScreenManager` class.
"""
class MDScreenManager(DeclarativeBehavior, ScreenManager):
    """
    Screen manager. This is the main class that will control your
    :class:`~kivymd.uix.screen.MDScreen` stack and memory.

    For more
    information, see in the :class:`~kivy.uix.screenmanager.ScreenManager`
    class documentation.
    """
    current_hero = ...
    current_heroes = ...
    _heroes_data = ...
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def check_transition(self, *args) -> None:
        """Sets the default type transition."""
        ...
    
    def get_hero_from_widget(self) -> list:
        """
        Get a list of :class:`~kivymd.uix.hero.MDHeroFrom` objects according
        to the tag names specified in the :attr:`~current_heroes` list.
        """
        ...
    
    def on_current_hero(self, instance, value: str) -> None:
        """
        Called when the value of the :attr:`current_hero` attribute changes.
        """
        ...
    
    def add_widget(self, widget, *args, **kwargs): # -> None:
        ...
    


