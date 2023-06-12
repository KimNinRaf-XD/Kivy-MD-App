"""
This type stub file was generated by pyright.
"""

from typing import NoReturn

"""
Behaviors/Ripple
================

.. rubric:: Classes implements a circular and rectangular ripple effects.

To create a widget with сircular ripple effect, you must create a new class
that inherits from the :class:`~CircularRippleBehavior` class.

For example, let's create an image button with a circular ripple effect:

.. code-block:: python

    from kivy.lang import Builder
    from kivy.uix.behaviors import ButtonBehavior
    from kivy.uix.image import Image

    from kivymd.app import MDApp
    from kivymd.uix.behaviors import CircularRippleBehavior

    KV = '''
    MDScreen:

        CircularRippleButton:
            source: "data/logo/kivy-icon-256.png"
            size_hint: None, None
            size: "250dp", "250dp"
            pos_hint: {"center_x": .5, "center_y": .5}
    '''


    class CircularRippleButton(CircularRippleBehavior, ButtonBehavior, Image):
        def __init__(self, **kwargs):
            self.ripple_scale = 0.85
            super().__init__(**kwargs)


    class Example(MDApp):
        def build(self):
            return Builder.load_string(KV)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/circular-ripple-effect.gif
    :align: center

To create a widget with rectangular ripple effect, you must create a new class
that inherits from the :class:`~RectangularRippleBehavior` class:

.. code-block:: python

    from kivy.lang import Builder
    from kivy.uix.behaviors import ButtonBehavior

    from kivymd.app import MDApp
    from kivymd.uix.behaviors import RectangularRippleBehavior, BackgroundColorBehavior

    KV = '''
    MDScreen:

        RectangularRippleButton:
            size_hint: None, None
            size: "250dp", "50dp"
            pos_hint: {"center_x": .5, "center_y": .5}
    '''


    class RectangularRippleButton(
        RectangularRippleBehavior, ButtonBehavior, BackgroundColorBehavior
    ):
        md_bg_color = [0, 0, 1, 1]


    class Example(MDApp):
        def build(self):
            return Builder.load_string(KV)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/rectangular-ripple-effect.gif
    :align: center
"""
__all__ = ("CommonRipple", "RectangularRippleBehavior", "CircularRippleBehavior")
class CommonRipple:
    """Base class for ripple effect."""
    ripple_rad_default = ...
    ripple_color = ...
    ripple_alpha = ...
    ripple_scale = ...
    ripple_duration_in_fast = ...
    ripple_duration_in_slow = ...
    ripple_duration_out = ...
    ripple_canvas_after = ...
    ripple_func_in = ...
    ripple_func_out = ...
    _ripple_rad = ...
    _doing_ripple = ...
    _finishing_ripple = ...
    _fading_out = ...
    _no_ripple_effect = ...
    _round_rad = ...
    def lay_canvas_instructions(self) -> NoReturn:
        ...
    
    def start_ripple(self) -> None:
        ...
    
    def finish_ripple(self) -> None:
        ...
    
    def fade_out(self, *args) -> None:
        ...
    
    def anim_complete(self, *args) -> None:
        ...
    
    def on_touch_down(self, touch): # -> bool | None:
        ...
    
    def call_ripple_animation_methods(self, touch) -> None:
        ...
    
    def on_touch_move(self, touch, *args):
        ...
    
    def on_touch_up(self, touch):
        ...
    


class RectangularRippleBehavior(CommonRipple):
    """Class implements a rectangular ripple effect."""
    ripple_scale = ...
    def lay_canvas_instructions(self) -> None:
        ...
    


class CircularRippleBehavior(CommonRipple):
    """Class implements a circular ripple effect."""
    ripple_scale = ...
    def lay_canvas_instructions(self) -> None:
        ...
    

