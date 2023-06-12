"""
This type stub file was generated by pyright.
"""

from kivy.event import EventDispatcher

"""
Code Navigation Behavior
========================

The :class:`~kivy.uix.bahviors.CodeNavigationBehavior` modifies navigation
behavior in the :class:`~kivy.uix.textinput.TextInput`, making it work like an
IDE instead of a word processor.

Using this mixin gives the TextInput the ability to recognize whitespace,
punctuation and case variations (e.g. CamelCase) when moving over text. It
is currently used by the :class:`~kivy.uix.codeinput.CodeInput` widget.
"""
__all__ = ("CodeNavigationBehavior",)

class CodeNavigationBehavior(EventDispatcher):
    """Code navigation behavior. Modifies the navigation behavior in TextInput
    to work like an IDE instead of a word processor. Please see the
    :mod:`code navigation behaviors module <kivy.uix.behaviors.codenavigation>`
    documentation for more information.

    .. versionadded:: 1.9.1
    """

    ...
