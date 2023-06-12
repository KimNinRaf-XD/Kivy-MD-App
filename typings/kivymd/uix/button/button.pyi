"""
This type stub file was generated by pyright.
"""

from typing import Union
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.floatlayout import FloatLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import CommonElevationBehavior, DeclarativeBehavior, RectangularRippleBehavior, RotateBehavior
from kivymd.uix.label import MDLabel
from kivymd.uix.tooltip import MDTooltip

"""
Components/Button
=================

.. seealso::

    `Material Design spec, Buttons <https://material.io/components/buttons>`_

    `Material Design spec, Buttons: floating action button <https://material.io/components/buttons-floating-action-button>`_

.. rubric:: Buttons allow users to take actions, and make choices,
    with a single tap.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/buttons.png
    :align: center

`KivyMD` provides the following button classes for use:

- MDIconButton_
- MDFloatingActionButton_
- MDFlatButton_
- MDRaisedButton_
- MDRectangleFlatButton_
- MDRectangleFlatIconButton_
- MDRoundFlatButton_
- MDRoundFlatIconButton_
- MDFillRoundFlatButton_
- MDFillRoundFlatIconButton_
- MDTextButton_
- MDFloatingActionButtonSpeedDial_

.. MDIconButton:
MDIconButton
------------

.. tabs::

    .. tab:: Declarative KV style

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.app import MDApp

            KV = '''
            MDScreen:

                MDIconButton:
                    icon: "language-python"
                    pos_hint: {"center_x": .5, "center_y": .5}
            '''


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivymd.app import MDApp
            from kivymd.uix.button import MDIconButton
            from kivymd.uix.screen import MDScreen


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return (
                        MDScreen(
                            MDIconButton(
                                icon="language-python",
                                pos_hint={"center_x": 0.5, "center_y": 0.5},
                            )
                        )
                    )


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-icon-button.png
    :align: center

The :class:`~MDIconButton.icon` parameter must have the name of the icon
from ``kivymd/icon_definitions.py`` file.

You can also use custom icons:

.. code-block:: kv

    MDIconButton:
        icon: "kivymd/images/logo/kivymd-icon-256.png"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-icon-custom-button.png
    :align: center

By default, :class:`~MDIconButton` button has a size ``(dp(48), dp (48))``.
Use :class:`~BaseButton.icon_size` attribute to resize the button:

.. code-block:: kv

    MDIconButton:
        icon: "android"
        icon_size: "64sp"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-icon-button-user-font-size.png
    :align: center

By default, the color of :class:`~MDIconButton`
(depending on the style of the application) is black or white.
You can change the color of :class:`~MDIconButton` as the text color
of :class:`~kivymd.uix.label.MDLabel`, substituting ``theme_icon_color`` for
``theme_text_color`` and ``icon_color`` for ``text_color``.

.. code-block:: kv

    MDIconButton:
        icon: "android"
        theme_icon_color: "Custom"
        icon_color: app.theme_cls.primary_color

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-icon-button-theme-text-color.png
    :align: center

.. MDFloatingActionButton:
MDFloatingActionButton
----------------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-floating-action-button.png
    :align: center

The above parameters for :class:`~MDIconButton` apply
to :class:`~MDFloatingActionButton`.

To change :class:`~MDFloatingActionButton` background, use the
``md_bg_color`` parameter:

.. code-block:: kv

    MDFloatingActionButton:
        icon: "android"
        md_bg_color: app.theme_cls.primary_color

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-floating-action-button-md-bg-color.png
    :align: center

Material design style 3
-----------------------

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.button import MDFloatingActionButton

    KV = '''
    MDScreen:
        md_bg_color: "#f7f2fa"

        MDBoxLayout:
            id: box
            spacing: "56dp"
            adaptive_size: True
            pos_hint: {"center_x": .5, "center_y": .5}
    '''


    class Example(MDApp):
        def build(self):
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette = "Orange"
            self.theme_cls.material_style = "M3"
            return Builder.load_string(KV)

        def on_start(self):
            data = {
                "standard": {"md_bg_color": "#fefbff", "text_color": "#6851a5"},
                "small": {"md_bg_color": "#e9dff7", "text_color": "#211c29"},
                "large": {"md_bg_color": "#f8d7e3", "text_color": "#311021"},
            }
            for type_button in data.keys():
                self.root.ids.box.add_widget(
                    MDFloatingActionButton(
                        icon="pencil",
                        type=type_button,
                        theme_icon_color="Custom",
                        md_bg_color=data[type_button]["md_bg_color"],
                        icon_color=data[type_button]["text_color"],
                    )
                )


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-floating-action-button-m3.png
    :align: center

.. MDFlatButton:
MDFlatButton
------------

To change the text color of: class:`~MDFlatButton` use the ``text_color`` parameter:

.. code-block:: kv

    MDFlatButton:
        text: "MDFlatButton"
        theme_text_color: "Custom"
        text_color: "orange"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-flat-button-text-color.png
    :align: center

Or use markup:

.. code-block:: kv

    MDFlatButton:
        text: "[color=#00ffcc]MDFlatButton[/color]"

To specify the font size and font name, use the parameters as in the usual
`Kivy` buttons:

.. code-block:: kv

    MDFlatButton:
        text: "MDFlatButton"
        font_size: "18sp"
        font_name: "path/to/font"

.. MDRaisedButton:
MDRaisedButton
--------------

This button is similar to the :class:`~MDFlatButton` button except that you
can set the background color for :class:`~MDRaisedButton`:

.. code-block:: kv

    MDRaisedButton:
        text: "MDRaisedButton"
        md_bg_color: "red"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-raised-button.png
    :align: center

.. MDRectangleFlatButton:
MDRectangleFlatButton
---------------------

.. code-block:: kv

    MDRectangleFlatButton:
        text: "MDRectangleFlatButton"
        theme_text_color: "Custom"
        text_color: "white"
        line_color: "red"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-rectangle-flat-button-md-bg-color.png
    :align: center

.. MDRectangleFlatIconButton:
MDRectangleFlatIconButton
-------------------------

Button parameters :class:`~MDRectangleFlatIconButton` are the same as
button :class:`~MDRectangleFlatButton`, with the addition of the
``theme_icon_color`` and ``icon_color`` parameters as for :class:`~MDIconButton`.

.. code-block:: kv

    MDRectangleFlatIconButton:
        icon: "android"
        text: "MDRectangleFlatIconButton"
        theme_text_color: "Custom"
        text_color: "white"
        line_color: "red"
        theme_icon_color: "Custom"
        icon_color: "orange"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-rectangle-flat-icon-button-custom.png
    :align: center

Without border
--------------

.. code-block:: python

    from kivymd.app import MDApp
    from kivymd.uix.screen import MDScreen
    from kivymd.uix.button import MDRectangleFlatIconButton


    class Example(MDApp):
        def build(self):
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette = "Orange"
            return (
                MDScreen(
                    MDRectangleFlatIconButton(
                        text="MDRectangleFlatIconButton",
                        icon="language-python",
                        line_color=(0, 0, 0, 0),
                        pos_hint={"center_x": .5, "center_y": .5},
                    )
                )
            )


    Example().run()

.. code-block:: kv

    MDRectangleFlatIconButton:
        text: "MDRectangleFlatIconButton"
        icon: "language-python"
        line_color: 0, 0, 0, 0
        pos_hint: {"center_x": .5, "center_y": .5}

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-rectangle-flat-icon-button-without-border.png
    :align: center

.. MDRoundFlatButton:
MDRoundFlatButton
-----------------

.. code-block:: kv

    MDRoundFlatButton:
        text: "MDRoundFlatButton"
        text_color: "white"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-round-flat-button-text-color.png
    :align: center

.. MDRoundFlatIconButton:
MDRoundFlatIconButton
---------------------

Button parameters :class:`~MDRoundFlatIconButton` are the same as
button :class:`~MDRoundFlatButton`, with the addition of the
``theme_icon_color`` and ``icon_color`` parameters as for :class:`~MDIconButton`:

.. code-block:: kv

    MDRoundFlatIconButton:
        text: "MDRoundFlatIconButton"
        icon: "android"
        text_color: "white"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-round-flat-icon-button.png
    :align: center

.. MDFillRoundFlatButton:
MDFillRoundFlatButton
---------------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-fill-round-flat-button.png
    :align: center

Button parameters :class:`~MDFillRoundFlatButton` are the same as
button :class:`~MDRaisedButton`.

.. MDFillRoundFlatIconButton:
MDFillRoundFlatIconButton
-------------------------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-fill-round-flat-icon-button.png
    :align: center

Button parameters :class:`~MDFillRoundFlatIconButton` are the same as
button :class:`~MDRaisedButton`, with the addition of the
``theme_icon_color`` and ``icon_color`` parameters as for :class:`~MDIconButton`.

.. note:: Notice that the width of the :class:`~MDFillRoundFlatIconButton`
    button matches the size of the button text.

.. MDTextButton:
MDTextButton
------------

.. code-block:: kv

    MDTextButton:
        text: "MDTextButton"
        custom_color: "white"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-text-button.png
    :align: center

.. MDFloatingActionButtonSpeedDial:
MDFloatingActionButtonSpeedDial
-------------------------------

.. Note:: See the full list of arguments in the class
    :class:`~MDFloatingActionButtonSpeedDial`.

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp

    KV = '''
    MDScreen:

        MDFloatingActionButtonSpeedDial:
            data: app.data
            root_button_anim: True
    '''


    class Example(MDApp):
        data = {
            'Python': 'language-python',
            'PHP': 'language-php',
            'C++': 'language-cpp',
        }

        def build(self):
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette = "Orange"
            return Builder.load_string(KV)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/MDFloatingActionButtonSpeedDial.gif
    :align: center

Or without KV Language:

.. tabs::

    .. tab:: Imperative python style

        .. code-block:: python

            from kivymd.uix.screen import MDScreen
            from kivymd.app import MDApp
            from kivymd.uix.button import MDFloatingActionButtonSpeedDial


            class Example(MDApp):
                data = {
                    'Python': 'language-python',
                    'PHP': 'language-php',
                    'C++': 'language-cpp',
                }

                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    screen = MDScreen()
                    speed_dial = MDFloatingActionButtonSpeedDial()
                    speed_dial.data = self.data
                    speed_dial.root_button_anim = True
                    screen.add_widget(speed_dial)
                    return screen


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivymd.uix.screen import MDScreen
            from kivymd.app import MDApp
            from kivymd.uix.button import MDFloatingActionButtonSpeedDial


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return (
                        MDScreen(
                            MDFloatingActionButtonSpeedDial(
                                data={
                                    'Python': 'language-python',
                                    'PHP': 'language-php',
                                    'C++': 'language-cpp',
                                },
                                root_button_anim=True,
                            )
                        )
                    )


            Example().run()

You can use various types of animation of labels for buttons on the stack:

.. code-block:: kv

    MDFloatingActionButtonSpeedDial:
        hint_animation: True

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/MDFloatingActionButtonSpeedDial-hint.gif
    :align: center

You can set your color values for background, text of buttons etc:

.. code-block:: kv

    MDFloatingActionButtonSpeedDial:
        hint_animation: True
        bg_hint_color: app.theme_cls.primary_dark

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/MDFloatingActionButtonSpeedDial-hint-color.png
    :align: center

Binds to individual buttons
---------------------------

.. tabs::

    .. tab:: Declarative KV style

        .. code-block:: python

            from kivy.lang import Builder
            from kivy.properties import DictProperty

            from kivymd.app import MDApp

            KV = '''
            MDScreen:

                MDFloatingActionButtonSpeedDial:
                    id: speed_dial
                    data: app.data
                    root_button_anim: True
                    hint_animation: True
            '''


            class Example(MDApp):
                data = DictProperty()

                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    self.data = {
                        'Python': 'language-python',
                        'JS': [
                            'language-javascript',
                            "on_press", lambda x: print("pressed JS"),
                            "on_release", lambda x: print(
                                "stack_buttons",
                                self.root.ids.speed_dial.stack_buttons
                            )
                        ],
                        'PHP': [
                            'language-php',
                            "on_press", lambda x: print("pressed PHP"),
                            "on_release", self.callback
                        ],
                        'C++': [
                            'language-cpp',
                            "on_press", lambda x: print("pressed C++"),
                            "on_release", lambda x: self.callback()
                        ],
                    }
                    return Builder.load_string(KV)

                def callback(self, *args):
                    print(args)


            Example().run()

    .. tab:: Declarative python style

        .. code-block:: python

            from kivymd.app import MDApp
            from kivymd.uix.button import MDFloatingActionButtonSpeedDial
            from kivymd.uix.screen import MDScreen


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return (
                        MDScreen(
                            MDFloatingActionButtonSpeedDial(
                                id="speed_dial",
                                hint_animation=True,
                                root_button_anim=True,
                            )
                        )
                    )

                def on_start(self):
                    data = {
                        "Python": "language-python",
                        "JS": [
                            "language-javascript",
                            "on_press", lambda x: print("pressed JS"),
                            "on_release", lambda x: print(
                                "stack_buttons",
                                self.root.ids.speed_dial.stack_buttons
                            )
                        ],
                        "PHP": [
                            "language-php",
                            "on_press", lambda x: print("pressed PHP"),
                            "on_release", self.callback
                        ],
                        "C++": [
                            "language-cpp",
                            "on_press", lambda x: print("pressed C++"),
                            "on_release", lambda x: self.callback()
                        ],
                    }
                    self.root.ids.speed_dial.data = data

                def callback(self, *args):
                    print(args)


            Example().run()
"""
__all__ = ("BaseButton", "MDIconButton", "MDFloatingActionButton", "MDFlatButton", "MDRaisedButton", "MDRectangleFlatButton", "MDRectangleFlatIconButton", "MDRoundFlatButton", "MDRoundFlatIconButton", "MDFillRoundFlatButton", "MDFillRoundFlatIconButton", "MDTextButton", "MDFloatingActionButtonSpeedDial")
theme_text_color_options = ...
class BaseButton(DeclarativeBehavior, RectangularRippleBehavior, ThemableBehavior, ButtonBehavior, AnchorLayout):
    """
    Base class for all buttons.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.DeclarativeBehavior` and
    :class:`~kivymd.uix.behaviors.RectangularRippleBehavior` and
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivy.uix.behaviors.ButtonBehavior` and
    :class:`~kivy.uix.anchorlayout.AnchorLayout`
    classes documentation.
    """
    padding = ...
    halign = ...
    valign = ...
    text = ...
    icon = ...
    font_style = ...
    theme_text_color = ...
    theme_icon_color = ...
    text_color = ...
    icon_color = ...
    font_name = ...
    font_size = ...
    icon_size = ...
    line_width = ...
    line_color = ...
    line_color_disabled = ...
    md_bg_color = ...
    md_bg_color_disabled = ...
    disabled_color = ...
    rounded_button = ...
    _radius = ...
    _disabled_color = ...
    _md_bg_color = ...
    _md_bg_color_disabled = ...
    _line_color = ...
    _line_color_disabled = ...
    _theme_text_color = ...
    _theme_icon_color = ...
    _text_color = ...
    _icon_color = ...
    _min_width = ...
    _min_height = ...
    _default_md_bg_color = ...
    _default_md_bg_color_disabled = ...
    _default_line_color = ...
    _default_line_color_disabled = ...
    _default_theme_text_color = ...
    _default_theme_icon_color = ...
    _default_text_color = ...
    _default_icon_color = ...
    _animation_fade_bg = ...
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def set_disabled_color(self, *args): # -> None:
        """
        Sets the color for the icon, text and line of the button when button
        is disabled.
        """
        ...
    
    def set_all_colors(self, *args) -> None:
        """Set all button colours."""
        ...
    
    def set_button_colors(self, *args) -> None:
        """Set all button colours (except text/icons)."""
        ...
    
    def set_text_color(self, *args) -> None:
        """
        Set _theme_text_color and _text_color based on defaults and options.
        """
        ...
    
    def set_icon_color(self, *args) -> None:
        """
        Set _theme_icon_color and _icon_color based on defaults and options.
        """
        ...
    
    def set_radius(self, *args) -> None:
        """
        Set the radius, if we are a rounded button, based on the
        current height.
        """
        ...
    
    def on_touch_down(self, touch): # -> Literal[False]:
        """
        Animates fade to background on press, for buttons with no
        background color.
        """
        ...
    
    def on_touch_up(self, touch):
        """Animates return to original background on touch release."""
        ...
    
    def on_disabled(self, instance_button, disabled_value: bool) -> None:
        ...
    


class ButtonElevationBehaviour(CommonElevationBehavior):
    """
    Implements elevation behavior as well as the recommended down/disabled
    colors for raised buttons.

    The minimum elevation for any raised button is `'1dp'`,
    by default, set to `'2dp'`.

    The `_elevation_raised` is automatically computed and is set to
    `self.elevation + 6` each time `self.elevation` is updated.
    """
    _elevation_raised = ...
    _anim_raised = ...
    _default_elevation = ...
    def __init__(self, **kwargs) -> None:
        ...
    
    def create_anim_raised(self, *args) -> None:
        ...
    
    def on_touch_down(self, touch): # -> Literal[False]:
        ...
    
    def on_touch_up(self, touch):
        ...
    
    def stop_elevation_anim(self): # -> None:
        ...
    


class ButtonContentsText:
    """Contents for :class:`~BaseButton` class consisting of a single label."""
    ...


class ButtonContentsIcon:
    """
    Contents for a round BaseButton consisting of an :class:`~MDIcon` class.
    """
    _min_width = ...
    def on_text_color(self, instance_button, color: list) -> None:
        """
        Set icon_color equal to text_color.
        For backwards compatibility - can use text_color instead
        of icon_color.
        """
        ...
    


class ButtonContentsIconText:
    """
    Contents for :class:`~BaseButton` class consisting of a
    :class:`~kivy.uix.boxlayout.BoxLayout` with an icon and a label.
    """
    padding = ...


class OldButtonIconMixin:
    """Backwards-compatibility for icons."""
    icon = ...
    def on_icon_color(self, instance_button, color: list) -> None:
        """
        If we are setting an icon color, set theme_icon_color to Custom.
        For backwards compatibility (before theme_icon_color existed).
        """
        ...
    


class MDFlatButton(BaseButton, ButtonContentsText):
    """
    A flat rectangular button with (by default) no border or background.
    Text is the default text color.

    For more information, see in the
    :class:`~BaseButton` and :class:`~ButtonContentsText`
    classes documentation.
    """
    padding = ...


class MDRaisedButton(BaseButton, ButtonElevationBehaviour, ButtonContentsText):
    """
    A flat button with (by default) a primary color fill and matching
    color text.

    For more information, see in the
    :class:`~BaseButton` and
    :class:`~ButtonElevationBehaviour` and
    :class:`~ButtonContentsText`
    classes documentation.
    """
    _default_md_bg_color = ...
    _default_md_bg_color_disabled = ...
    _default_theme_text_color = ...
    _default_text_color = ...
    def __init__(self, *args, **kwargs) -> None:
        ...
    


class MDRectangleFlatButton(BaseButton, ButtonContentsText):
    """
    A flat button with (by default) a primary color border and primary
    color text.

    For more information, see in the
    :class:`~BaseButton` and :class:`~ButtonContentsText`
    classes documentation.
    """
    _default_line_color = ...
    _default_line_color_disabled = ...
    _default_theme_text_color = ...
    _default_text_color = ...


class MDRectangleFlatIconButton(BaseButton, OldButtonIconMixin, ButtonContentsIconText):
    """
    A flat button with (by default) a primary color border, primary color text
    and a primary color icon on the left.

    For more information, see in the
    :class:`~BaseButton` and
    :class:`~OldButtonIconMixin` and
    :class:`~ButtonContentsIconText`
    classes documentation.
    """
    _default_line_color = ...
    _default_line_color_disabled = ...
    _default_theme_text_color = ...
    _default_theme_icon_color = ...
    _default_text_color = ...
    _default_icon_color = ...


class MDRoundFlatButton(BaseButton, ButtonContentsText):
    """
    A flat button with (by default) fully rounded corners, a primary
    color border and primary color text.

    For more information, see in the
    :class:`~BaseButton` and :class:`~ButtonContentsText`
    classes documentation.
    """
    _default_line_color = ...
    _default_line_color_disabled = ...
    _default_theme_text_color = ...
    _default_text_color = ...
    def __init__(self, *args, **kwargs) -> None:
        ...
    


class MDRoundFlatIconButton(BaseButton, OldButtonIconMixin, ButtonContentsIconText):
    """
    A flat button with (by default) rounded corners, a primary color border,
    primary color text and a primary color icon on the left.

    For more information, see in the
    :class:`~BaseButton` and
    :class:`~OldButtonIconMixin` and
    :class:`~ButtonContentsIconText`
    classes documentation.
    """
    _default_line_color = ...
    _default_line_color_disabled = ...
    _default_theme_text_color = ...
    _default_theme_icon_color = ...
    _default_text_color = ...
    _default_icon_color = ...
    def __init__(self, *args, **kwargs) -> None:
        ...
    


class MDFillRoundFlatButton(BaseButton, ButtonContentsText):
    """
    A flat button with (by default) rounded corners, a primary color fill
    and primary color text.

    For more information, see in the
    :class:`~BaseButton` and :class:`~ButtonContentsText`
    classes documentation.
    """
    _default_md_bg_color = ...
    _default_md_bg_color_disabled = ...
    _default_theme_text_color = ...
    _default_text_color = ...
    def __init__(self, *args, **kwargs) -> None:
        ...
    


class MDFillRoundFlatIconButton(BaseButton, OldButtonIconMixin, ButtonContentsIconText):
    """
    A flat button with (by default) rounded corners, a primary color fill,
    primary color text and a primary color icon on the left.

    For more information, see in the
    :class:`~BaseButton` and
    :class:`~OldButtonIconMixin` and
    :class:`~ButtonContentsIconText`
    classes documentation.
    """
    _default_md_bg_color = ...
    _default_md_bg_color_disabled = ...
    _default_theme_text_color = ...
    _default_theme_icon_color = ...
    _default_text_color = ...
    _default_icon_color = ...
    def __init__(self, *args, **kwargs) -> None:
        ...
    


class MDIconButton(BaseButton, OldButtonIconMixin, ButtonContentsIcon):
    """
    A simple rounded icon button.

    For more information, see in the
    :class:`~BaseButton` and
    :class:`~OldButtonIconMixin` and
    :class:`~ButtonContentsIcon` classes documentation.
    """
    icon = ...
    _min_width = ...
    _default_icon_pad = ...
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def set_size(self, interval: Union[int, float]) -> None:
        """
        Sets the icon width/height based on the current `icon_size`
        attribute, or the default value if it is zero. The icon size
        is set to `(48, 48)` for an icon with the default font_size 24sp.
        """
        ...
    


class MDFloatingActionButton(BaseButton, OldButtonIconMixin, ButtonElevationBehaviour, ButtonContentsIcon):
    """
    Implementation
    `FAB <https://m3.material.io/components/floating-action-button/overview>`_
    button.

    For more information, see in the
    :class:`~BaseButton` and
    :class:`~OldButtonIconMixin` and
    :class:`~ButtonElevationBehaviour` and
    :class:`~ButtonContentsIcon` classes documentation.
    """
    type = ...
    _default_md_bg_color = ...
    _default_md_bg_color_disabled = ...
    _default_theme_icon_color = ...
    _default_icon_color = ...
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def set_font_size(self, *args) -> None:
        ...
    
    def set__radius(self, *args) -> None:
        ...
    
    def set_size_and_radius(self, *args) -> None:
        ...
    
    def set_size(self, *args) -> None:
        ...
    
    def on_type(self, instance_md_floating_action_button, type: str) -> None:
        ...
    


class MDTextButton(ButtonBehavior, MDLabel):
    """
    Text button class.

    For more information, see in the
    :class:`~kivy.uix.behaviors.ButtonBehavior` and
    :class:`~kivymd.uix.label.MDLabel` classes documentation.
    """
    color = ...
    color_disabled = ...
    _color = ...
    def animation_label(self) -> None:
        ...
    
    def on_press(self, *args):
        ...
    
    def on_disabled(self, instance_button, disabled_value) -> None:
        ...
    


class BaseFloatingBottomButton(MDFloatingActionButton, MDTooltip):
    _canvas_width = ...
    _padding_right = ...
    _bg_color = ...
    def set_size(self, interval: Union[int, float]) -> None:
        ...
    


class MDFloatingBottomButton(BaseFloatingBottomButton):
    _bg_color = ...


class MDFloatingRootButton(RotateBehavior, MDFloatingActionButton):
    rotate_value_angle = ...


class MDFloatingLabel(MDLabel):
    bg_color = ...


class MDFloatingActionButtonSpeedDial(DeclarativeBehavior, ThemableBehavior, FloatLayout):
    """
    For more information, see in the
    :class:`~kivy.uix.floatlayout.FloatLayout` class documentation.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.DeclarativeBehavior` and
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivy.uix.floatlayout.FloatLayout`
    lasses documentation.

    :Events:
        :attr:`on_open`
            Called when a stack is opened.
        :attr:`on_close`
            Called when a stack is closed.
        :attr:`on_press_stack_button`
            Called at the on_press event for the stack button.
        :attr:`on_release_stack_button`
            Called at the on_press event for the stack button.
    """
    icon = ...
    anchor = ...
    label_text_color = ...
    label_bg_color = ...
    label_radius = ...
    data = ...
    right_pad = ...
    right_pad_value = ...
    root_button_anim = ...
    opening_transition = ...
    closing_transition = ...
    opening_transition_button_rotation = ...
    closing_transition_button_rotation = ...
    opening_time = ...
    closing_time = ...
    opening_time_button_rotation = ...
    closing_time_button_rotation = ...
    state = ...
    bg_color_root_button = ...
    bg_color_stack_button = ...
    color_icon_stack_button = ...
    color_icon_root_button = ...
    bg_hint_color = ...
    hint_animation = ...
    stack_buttons = ...
    _label_pos_y_set = ...
    _anim_buttons_data = ...
    _anim_labels_data = ...
    def __init__(self, **kwargs) -> None:
        ...
    
    def on_open(self, *args): # -> None:
        """Called when a stack is opened."""
        ...
    
    def on_close(self, *args): # -> None:
        """Called when a stack is closed."""
        ...
    
    def on_leave(self, instance_button: MDFloatingBottomButton) -> None:
        """Called when the mouse cursor goes outside the button of stack."""
        ...
    
    def on_enter(self, instance_button: MDFloatingBottomButton) -> None:
        """Called when the mouse cursor is over a button from the stack."""
        ...
    
    def on_data(self, instance_speed_dial, data: dict) -> None:
        """Creates a stack of buttons."""
        ...
    
    def on_icon(self, instance_speed_dial, name_icon: str) -> None:
        ...
    
    def on_label_text_color(self, instance_speed_dial, color: list | str) -> None:
        ...
    
    def on_color_icon_stack_button(self, instance_speed_dial, color: list) -> None:
        ...
    
    def on_hint_animation(self, instance_speed_dial, value: bool) -> None:
        ...
    
    def on_bg_hint_color(self, instance_speed_dial, color: list) -> None:
        ...
    
    def on_color_icon_root_button(self, instance_speed_dial, color: list) -> None:
        ...
    
    def on_bg_color_stack_button(self, instance_speed_dial, color: list) -> None:
        ...
    
    def on_bg_color_root_button(self, instance_speed_dial, color: list) -> None:
        ...
    
    def on_press_stack_button(self, *args) -> None:
        """
        Called at the on_press event for the stack button.

        .. code-block:: kv

            MDFloatingActionButtonSpeedDial:
                on_press_stack_button: print(*args)

        .. versionadded:: 1.1.0
        """
        ...
    
    def on_release_stack_button(self, *args) -> None:
        """
        Called at the on_release event for the stack button.

        .. code-block:: kv

            MDFloatingActionButtonSpeedDial:
                on_release_stack_button: print(*args)

        .. versionadded:: 1.1.0
        """
        ...
    
    def set_pos_labels(self, instance_floating_label: MDFloatingLabel) -> None:
        """
        Sets the position of the floating labels.
        Called when the application's root window is resized.
        """
        ...
    
    def set_pos_root_button(self, instance_floating_root_button: MDFloatingRootButton) -> None:
        """
        Sets the position of the root button.
        Called when the application's root window is resized.
        """
        ...
    
    def set_pos_bottom_buttons(self, instance_floating_bottom_button: MDFloatingBottomButton) -> None:
        """
        Sets the position of the bottom buttons in a stack.
        Called when the application's root window is resized.
        """
        ...
    
    def open_stack(self, instance_floating_root_button: MDFloatingRootButton) -> None:
        """Opens a button stack."""
        ...
    
    def do_animation_open_stack(self, anim_data: dict) -> None:
        """
        :param anim_data:
            {
                <kivymd.uix.button.MDFloatingBottomButton object>:
                    <kivy.animation.Animation>,
                <kivymd.uix.button.MDFloatingBottomButton object>:
                    <kivy.animation.Animation object>,
                ...,
            }
        """
        ...
    
    def close_stack(self): # -> None:
        """Closes the button stack."""
        ...
    


