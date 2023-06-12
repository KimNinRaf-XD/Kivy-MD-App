"""
This type stub file was generated by pyright.
"""

from kivy.uix.screenmanager import SlideTransition, SwapTransition, TransitionBase
from kivymd.uix.screenmanager import MDScreenManager

"""
Components/Transition
=====================

.. rubric::
    A set of classes for implementing transitions between application screens.

.. versionadded:: 1.0.0

Changing transitions
--------------------

You have multiple transitions available by default, such as:

- :class:`MDFadeSlideTransition`
    state one: the new screen closes the previous screen by lifting from the
    bottom of the screen and changing from transparent to non-transparent;

    state two: the current screen goes down to the bottom of the screen,
    passing from a non-transparent state to a transparent one, thus opening the
    previous screen;

.. note::
    You cannot control the direction of a slide using the direction attribute.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/transition-md-fade-slide-transition.gif
    :align: center

"""
__all__ = ("MDFadeSlideTransition", "MDSlideTransition", "MDSwapTransition", "MDTransitionBase")
class MDTransitionBase(TransitionBase):
    """
    TransitionBase is used to animate 2 screens within the
    :class:`~kivymd.uix.screenmanager.MDScreenManager`.

    For more
    information, see in the :class:`~kivy.uix.screenmanager.TransitionBase`
    class documentation.
    """
    _direction = ...
    _hero_from_widget_children = ...
    def start(self, instance_screen_manager: MDScreenManager) -> None:
        ...
    
    def animated_hero_in(self) -> None:
        """Animates the flight of heroes from screen **A** to screen **B**."""
        ...
    
    def animated_hero_out(self) -> None:
        """Animates the flight of heroes from screen **B** to screen **A**."""
        ...
    
    def on_complete(self) -> None:
        """
        Override method.
        See :attr:`kivy.uix.screenmanager.TransitionBase.on_complete'.
        """
        ...
    


class MDSwapTransition(SwapTransition, MDTransitionBase):
    ...


class MDSlideTransition(SlideTransition, MDTransitionBase):
    ...


class MDFadeSlideTransition(MDSlideTransition):
    def start(self, instance_screen_manager: MDScreenManager) -> None:
        ...
    
    def on_progress(self, progression: float) -> None:
        ...
    

