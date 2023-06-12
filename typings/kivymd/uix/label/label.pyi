"""
This type stub file was generated by pyright.
"""

from typing import Union
from kivy.uix.label import Label
from kivymd.theming import ThemableBehavior
from kivymd.uix import MDAdaptiveWidget
from kivymd.uix.behaviors import DeclarativeBehavior, TouchBehavior
from kivymd.uix.floatlayout import MDFloatLayout

"""
Components/Label
================

.. rubric:: The :class:`MDLabel` widget is for rendering text.

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/label.png
    :align: center

- MDLabel_
- MDIcon_

.. MDLabel:
MDLabel
-------

Class :class:`MDLabel` inherited from the :class:`~kivy.uix.label.Label` class
but for :class:`MDLabel` the ``text_size`` parameter is ``(self.width, None)``
and default is positioned on the left:

.. tabs::

    .. tab:: Declarative KV style

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.app import MDApp

            KV = '''
            MDScreen:

                MDLabel:
                    text: "MDLabel"
            '''


            class Test(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return Builder.load_string(KV)


            Test().run()

    .. tab:: Declarative Python style

        .. code-block:: python

            from kivy.lang import Builder

            from kivymd.app import MDApp
            from kivymd.uix.screen import MDScreen
            from kivymd.uix.label import MDLabel


            class Test(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return (
                        MDScreen(
                            MDLabel(
                                text="MDLabel"
                            )
                        )
                    )


            Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-label-to-left.png
    :align: center

.. Note:: See :attr:`~kivy.uix.label.Label.halign`
    and :attr:`~kivy.uix.label.Label.valign` attributes
    of the :class:`~kivy.uix.label.Label` class

.. code-block:: kv

        MDLabel:
            text: "MDLabel"
            halign: "center"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-label-to-center.png
    :align: center

:class:`~MDLabel` color:
------------------------

:class:`~MDLabel` provides standard color themes for label color management:

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.label import MDLabel

    KV = '''
    MDBoxLayout:
        orientation: "vertical"
    '''


    class Test(MDApp):
        def build(self):
            self.theme_cls.theme_style = "Dark"
            screen = Builder.load_string(KV)

            # Names of standard color themes.
            for name_theme in [
                "Primary",
                "Secondary",
                "Hint",
                "Error",
                "ContrastParentBackground",
            ]:
                screen.add_widget(
                    MDLabel(
                        text=name_theme,
                        halign="center",
                        theme_text_color=name_theme,
                    )
                )
            return screen


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-label-theme-text-color.png
    :align: center

To use a custom color for :class:`~MDLabel`, use a theme `'Custom'`.
After that, you can specify the desired color in the ``rgba`` format
in the ``text_color`` parameter:

.. code-block:: kv

    MDLabel:
        text: "Custom color"
        halign: "center"
        theme_text_color: "Custom"
        text_color: "blue"

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-label-custom-color.png
    :align: center

:class:`~MDLabel` provides standard font styles for labels. To do this,
specify the name of the desired style in the :attr:`~MDLabel.font_style`
parameter:

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp
    from kivymd.uix.label import MDLabel
    from kivymd.font_definitions import theme_font_styles

    KV = '''
    MDScrollView:

        MDList:
            id: box
            spacing: "8dp"
    '''


    class Test(MDApp):
        def build(self):
            self.theme_cls.theme_style = "Dark"
            screen = Builder.load_string(KV)

            # Names of standard font styles.
            for name_style in theme_font_styles[:-1]:
                screen.ids.box.add_widget(
                    MDLabel(
                        text=f"{name_style} style",
                        halign="center",
                        font_style=name_style,
                        adaptive_height=True,
                    )
                )
            return screen


    Test().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-label-font-style.png
    :align: center

Highlighting and copying labels
===============================

You can highlight labels by double tap on the label:
----------------------------------------------------

.. tabs::

    .. tab:: Declarative KV style

        .. code-block:: python

            from kivy.lang.builder import Builder

            from kivymd.app import MDApp

            KV = '''
            MDScreen:

                MDLabel:
                    adaptive_size: True
                    pos_hint: {"center_x": .5, "center_y": .5}
                    text: "MDLabel"
                    allow_selection: True
                    padding: "4dp", "4dp"
            '''


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative Python style

        .. code-block:: python

            from kivy.lang.builder import Builder

            from kivymd.app import MDApp
            from kivymd.uix.label import MDLabel
            from kivymd.uix.screen import MDScreen


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return (
                        MDScreen(
                            MDLabel(
                                adaptive_size=True,
                                pos_hint={"center_x": .5, "center_y": .5},
                                text="MDLabel",
                                allow_selection=True,
                                padding=("4dp", "4dp"),
                            )
                        )
                    )


            Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-label-allow-selection.gif
    :align: center

You can copy the label text by double clicking on it:
-----------------------------------------------------

.. tabs::

    .. tab:: Declarative KV style

        .. code-block:: python

            from kivy.lang.builder import Builder

            from kivymd.app import MDApp

            KV = '''
            MDScreen:

                MDLabel:
                    adaptive_size: True
                    pos_hint: {"center_x": .5, "center_y": .5}
                    text: "MDLabel"
                    padding: "4dp", "4dp"
                    allow_selection: True
                    allow_copy: True
                    on_copy: print("The text is copied to the clipboard")
            '''


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return Builder.load_string(KV)


            Example().run()

    .. tab:: Declarative Python style

        .. code-block:: python

            from kivy.lang.builder import Builder

            from kivymd.app import MDApp
            from kivymd.uix.label import MDLabel
            from kivymd.uix.screen import MDScreen


            class Example(MDApp):
                def build(self):
                    self.theme_cls.theme_style = "Dark"
                    self.theme_cls.primary_palette = "Orange"
                    return (
                        MDScreen(
                            MDLabel(
                                id="label",
                                adaptive_size=True,
                                pos_hint={"center_x": .5, "center_y": .5},
                                text="MDLabel",
                                allow_selection=True,
                                allow_copy=True,
                                padding=("4dp", "4dp"),
                            )
                        )
                    )

                def on_start(self):
                    self.root.ids.label.bind(on_copy=self.on_copy)

                def on_copy(self, instance_label: MDLabel):
                    print("The text is copied to the clipboard")


            Example().run()

Example of copying/cutting labels using the context menu
--------------------------------------------------------

.. code-block:: python

    from kivy.core.clipboard import Clipboard
    from kivy.lang.builder import Builder
    from kivy.metrics import dp

    from kivymd.app import MDApp
    from kivymd.uix.label import MDLabel
    from kivymd.uix.menu import MDDropdownMenu
    from kivymd.toast import toast

    KV = '''
    MDBoxLayout:
        orientation: "vertical"
        spacing: "12dp"
        padding: "24dp"

        MDScrollView:

            MDBoxLayout:
                id: box
                orientation: "vertical"
                padding: "24dp"
                spacing: "12dp"
                adaptive_height: True

        MDTextField:
            max_height: "200dp"
            mode: "fill"
            multiline: True

        MDWidget:
    '''

    data = [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "Sed blandit libero volutpat sed cras ornare arcu. Nisl vel pretium "
        "lectus quam id leo in. Tincidunt arcu non sodales neque sodales ut etiam.",
        "Elit scelerisque mauris pellentesque pulvinar pellentesque habitant. "
        "Nisl rhoncus mattis rhoncus urna neque. Orci nulla pellentesque "
        "dignissim enim. Ac auctor augue mauris augue neque gravida in fermentum. "
        "Lacus suspendisse faucibus interdum posuere."

    ]


    class CopyLabel(MDLabel):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.allow_selection = True
            self.adaptive_height = True
            self.theme_text_color = "Custom"
            self.text_color = self.theme_cls.text_color


    class Example(MDApp):
        context_menu = None

        def build(self):
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette = "Orange"
            return Builder.load_string(KV)

        def on_start(self):
            for text in data:
                copy_label = CopyLabel(text=text)
                copy_label.bind(
                    on_selection=self.open_context_menu,
                    on_cancel_selection=self.restore_text_color,
                )
                self.root.ids.box.add_widget(copy_label)

        def click_item_context_menu(
            self, type_click: str, instance_label: CopyLabel
        ) -> None:
            Clipboard.copy(instance_label.text)

            if type_click == "copy":
                toast("Copied")
            elif type_click == "cut":
                self.root.ids.box.remove_widget(instance_label)
                toast("Cut")
            if self.context_menu:
                self.context_menu.dismiss()

        def restore_text_color(self, instance_label: CopyLabel) -> None:
            instance_label.text_color = self.theme_cls.text_color

        def open_context_menu(self, instance_label: CopyLabel) -> None:
            instance_label.text_color = "black"
            menu_items = [
                {
                    "text": "Copy text",
                    "viewclass": "OneLineListItem",
                    "height": dp(48),
                    "on_release": lambda: self.click_item_context_menu(
                        "copy", instance_label
                    ),
                },
                {
                    "text": "Cut text",
                    "viewclass": "OneLineListItem",
                    "height": dp(48),
                    "on_release": lambda: self.click_item_context_menu(
                        "cut", instance_label
                    ),
                },
            ]
            self.context_menu = MDDropdownMenu(
                caller=instance_label, items=menu_items, width_mult=3
            )
            self.context_menu.open()


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/copying-cutting-labels-using-context-menu.gif
    :align: center

.. MDIcon:
MDIcon
-------

You can use labels to display material design icons using the
:class:`~MDIcon` class.

.. seealso::

    `Material Design Icons <https://materialdesignicons.com/>`_

    `Material Design Icon Names <https://github.com/kivymd/KivyMD/blob/master/kivymd/icon_definitions.py>`_

The :class:`~MDIcon` class is inherited from
:class:`~MDLabel` and has the same parameters.

.. Warning:: For the :class:`~MDIcon` class, you cannot use ``text``
    and ``font_style`` options!

.. code-block:: kv

    MDIcon:
        icon: "gmail"
        pos_hint: {"center_x": .5, "center_y": .5}

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-icon.png
    :align: center

MDIcon with badge icon
----------------------

.. code-block:: kv

    MDIcon:
        icon: "gmail"
        badge_icon: "numeric-10"
        pos_hint: {"center_x": .5, "center_y": .5}

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-icon-badge.png
    :align: center
"""
__all__ = ("MDLabel", "MDIcon")
__MDLabel_colors__ = ...
class MDLabel(DeclarativeBehavior, ThemableBehavior, Label, MDAdaptiveWidget, TouchBehavior):
    """
    Label class.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.DeclarativeBehavior` and
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivy.uix.label.Label` and
    :class:`~kivymd.uix.MDAdaptiveWidget` and
    :class:`~kivymd.uix.behaviors.TouchBehavior`
    classes documentation.

    :Events:
        `on_ref_press`
            Called when the user clicks on a word referenced with a
            ``[ref]`` tag in a text markup.
        `on_copy`
            Called when double-tapping on the label.
        `on_selection`
            Called when double-tapping on the label.
        `on_cancel_selection`
            Called when the highlighting is removed from the label text.
    """
    font_style = ...
    _capitalizing = ...
    _text = ...
    text = ...
    theme_text_color = ...
    text_color = ...
    allow_copy = ...
    allow_selection = ...
    color_selection = ...
    color_deselection = ...
    is_selected = ...
    _text_color_str = ...
    parent_background = ...
    can_capitalize = ...
    canvas_bg = ...
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def check_font_styles(self, interval: Union[int, float] = ...) -> bool:
        ...
    
    def update_font_style(self, instance_label, font_style: str) -> None:
        ...
    
    def do_selection(self) -> None:
        ...
    
    def cancel_selection(self) -> None:
        ...
    
    def on_double_tap(self, touch, *args) -> None:
        ...
    
    def on_window_touch(self, *args): # -> None:
        ...
    
    def on_copy(self, *args) -> None:
        """
        Called when double-tapping on the label.

        .. versionadded:: 1.2.0
        """
        ...
    
    def on_selection(self, *args) -> None:
        """
        Called when double-tapping on the label.

        .. versionadded:: 1.2.0
        """
        ...
    
    def on_cancel_selection(self, *args) -> None:
        """
        Called when the highlighting is removed from the label text.

        .. versionadded:: 1.2.0
        """
        ...
    
    def on_allow_selection(self, instance_label, selection: bool) -> None:
        ...
    
    def on_theme_text_color(self, instance_label, theme_text_color: str) -> None:
        ...
    
    def on_text_color(self, instance_label, color: Union[list, str]) -> None:
        ...
    
    def on_opposite_colors(self, *args) -> None:
        ...
    
    def on_md_bg_color(self, instance_label, color: Union[list, str]) -> None:
        ...
    
    def on_size(self, instance_label, size: list) -> None:
        ...
    
    def update_canvas_bg_pos(self, instance_label, pos: list) -> None:
        ...
    


class MDIcon(MDFloatLayout, MDLabel):
    """
    Icon class.

    For more information, see in the :class:`~MDLabel` and
    :class:`~kivymd.uix.floatlayout.MDFloatLayout` classes documentation.
    """
    icon = ...
    badge_icon = ...
    badge_icon_color = ...
    badge_bg_color = ...
    badge_font_size = ...
    source = ...
    _size = ...
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def adjust_size(self, *args) -> None:
        ...
    


