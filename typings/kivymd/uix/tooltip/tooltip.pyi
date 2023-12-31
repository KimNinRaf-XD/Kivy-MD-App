"""
This type stub file was generated by pyright.
"""

from typing import Union
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import HoverBehavior, TouchBehavior

"""
Components/Tooltip
==================

.. seealso::

    `Material Design spec, Tooltips <https://material.io/components/tooltips>`_

.. rubric:: Tooltips display informative text when users hover over, focus on,
    or tap an element.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tooltip.png
    :align: center

To use the :class:`~MDTooltip` class, you must create a new class inherited
from the :class:`~MDTooltip` class:

In Kv-language:

.. code-block:: kv

    <TooltipMDIconButton@MDIconButton+MDTooltip>

In Python code:

.. code-block:: python

    class TooltipMDIconButton(MDIconButton, MDTooltip):
        pass

.. Warning:: :class:`~MDTooltip` only works correctly with button and label classes.

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp

    KV = '''
    <TooltipMDIconButton@MDIconButton+MDTooltip>


    MDScreen:

        TooltipMDIconButton:
            icon: "language-python"
            tooltip_text: self.icon
            pos_hint: {"center_x": .5, "center_y": .5}
    '''


    class Test(MDApp):
        def build(self):
            return Builder.load_string(KV)


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/tooltip.gif
    :align: center

.. Note:: The behavior of tooltips on desktop and mobile devices is different.
    For more detailed information,
    `click here <https://github.com/kivymd/KivyMD/wiki/Components-Tooltips>`_.
"""
__all__ = ("MDTooltip", "MDTooltipViewClass")
class MDTooltip(ThemableBehavior, HoverBehavior, TouchBehavior):
    """
    Tooltip class.

    For more information, see in the
    :class:`~kivymd.theming.ThemableBehavior and
    :class:`~kivymd.uix.behaviors.HoverBehavior` and
    :class:`~kivymd.uix.behaviors.TouchBehavior`
    classes documentation.
    """
    tooltip_bg_color = ...
    tooltip_text_color = ...
    tooltip_text = ...
    tooltip_font_style = ...
    tooltip_radius = ...
    tooltip_display_delay = ...
    shift_y = ...
    shift_right = ...
    shift_left = ...
    _tooltip = ...
    def __init__(self, **kwargs) -> None:
        ...
    
    def delete_clock(self, widget, touch, *args): # -> None:
        ...
    
    def adjust_tooltip_position(self, x: float, y: float) -> tuple:
        """
        Returns the coordinates of the tooltip that fit into the borders of the
        screen.
        """
        ...
    
    def display_tooltip(self, interval: Union[int, float]) -> None:
        ...
    
    def animation_tooltip_show(self, interval: Union[int, float]) -> None:
        """Animation of opening tooltip on the screen."""
        ...
    
    def animation_tooltip_dismiss(self, interval: Union[int, float]) -> None:
        """
        .. versionadded:: 1.0.0

        Animation of closing tooltip on the screen.
        """
        ...
    
    def remove_tooltip(self, *args) -> None:
        """Removes the tooltip widget from the screen."""
        ...
    
    def on_long_touch(self, touch, *args) -> None:
        ...
    
    def on_enter(self, *args) -> None:
        """
        See
        :attr:`~kivymd.uix.behaviors.hover_behavior.HoverBehavior.on_enter`
        method in :class:`~kivymd.uix.behaviors.hover_behavior.HoverBehavior`
        class.
        """
        ...
    
    def on_leave(self) -> None:
        """
        See
        :attr:`~kivymd.uix.behaviors.hover_behavior.HoverBehavior.on_leave`
        method in :class:`~kivymd.uix.behaviors.hover_behavior.HoverBehavior`
        class.
        """
        ...
    
    def on_show(self) -> None:
        """Default display event handler."""
        ...
    
    def on_dismiss(self) -> None:
        """
        .. versionadded:: 1.0.0

        Default dismiss event handler.
        """
        ...
    


class MDTooltipViewClass(ThemableBehavior, BoxLayout):
    """
    Tooltip view class.

    For more information, see in the
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivy.uix.boxlayout.BoxLayout`
    classes documentation.
    """
    tooltip_bg_color = ...
    tooltip_text_color = ...
    tooltip_text = ...
    tooltip_font_style = ...
    tooltip_radius = ...
    _scale_x = ...
    _scale_y = ...
    def __init__(self, **kwargs) -> None:
        ...
    


