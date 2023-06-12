"""
This type stub file was generated by pyright.
"""

from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.floatlayout import FloatLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import CircularRippleBehavior, CommonElevationBehavior, ScaleBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDIcon

"""
Components/SelectionControls
============================

.. seealso::

    `Material Design spec, Checkbox <https://m3.material.io/components/checkbox/overview>`_

    `Material Design spec, Switch <https://m3.material.io/components/switch/overview>`_

.. rubric:: Selection controls allow the user to select options.

`KivyMD` provides the following selection controls classes for use:

- MDCheckbox_
- MDSwitch_

.. MDCheckbox:
MDCheckbox
----------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/checkbox.png
    :align: center

Usage
-----

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp


    KV = '''
    MDFloatLayout:

        MDCheckbox:
            size_hint: None, None
            size: "48dp", "48dp"
            pos_hint: {'center_x': .5, 'center_y': .5}
    '''


    class Example(MDApp):
        def build(self):
            self.theme_cls.primary_palette = "Green"
            self.theme_cls.theme_style = "Dark"
            return Builder.load_string(KV)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/checkbox.gif
    :align: center

.. Note:: Be sure to specify the size of the checkbox. By default, it is
    `(dp(48), dp(48))`, but the ripple effect takes up all the available
    space.

Control state
-------------

.. code-block:: kv

    MDCheckbox:
        on_active: app.on_checkbox_active(*args)

.. code-block:: python

    def on_checkbox_active(self, checkbox, value):
        if value:
            print('The checkbox', checkbox, 'is active', 'and', checkbox.state, 'state')
        else:
            print('The checkbox', checkbox, 'is inactive', 'and', checkbox.state, 'state')

MDCheckbox with group
---------------------

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp

    KV = '''
    <Check@MDCheckbox>:
        group: 'group'
        size_hint: None, None
        size: dp(48), dp(48)


    MDFloatLayout:

        Check:
            active: True
            pos_hint: {'center_x': .4, 'center_y': .5}

        Check:
            pos_hint: {'center_x': .6, 'center_y': .5}
    '''


    class Example(MDApp):
        def build(self):
            self.theme_cls.primary_palette = "Green"
            self.theme_cls.theme_style = "Dark"
            return Builder.load_string(KV)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/checkbox-group.gif
    :align: center

Parent and child checkboxes
---------------------------

Checkboxes can have a parent-child relationship with other checkboxes. When
the parent checkbox is checked, all child checkboxes are checked. If a parent
checkbox is unchecked, all child checkboxes are unchecked. If some, but not all,
child checkboxes are checked, the parent checkbox becomes an indeterminate
checkbox.

Usage
-----

.. code-block:: kv

    MDCheckbox:
        group: "root"  # this is a required name for the parent checkbox group

    MDCheckbox:
        group: "child"  # this is a required name for a group of child checkboxes

    MDCheckbox:
        group: "child"  # this is a required name for a group of child checkboxes

Example
-------

.. code-block:: python

    from kivy.lang import Builder
    from kivy.properties import StringProperty

    from kivymd.app import MDApp
    from kivymd.uix.boxlayout import MDBoxLayout

    KV = '''
    <CheckItem>
        adaptive_height: True

        MDCheckbox:
            size_hint: None, None
            size: "48dp", "48dp"
            group: root.group

        MDLabel:
            text: root.text
            adaptive_height: True
            theme_text_color: "Custom"
            text_color: "#B2B6AE"
            pos_hint: {"center_y": .5}


    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: "#141612"

        MDTopAppBar:
            md_bg_color: "#21271F"
            specific_text_color: "#B2B6AE"
            elevation: 0
            title: "Meal options"
            left_action_items: [["arrow-left", lambda x: x]]
            anchor_title: "left"

        MDBoxLayout:
            orientation: "vertical"
            adaptive_height: True
            padding: "12dp", "36dp", 0, 0

            CheckItem:
                text: "Recieve emails"
                group: "root"

            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                padding: "24dp", 0, 0, 0

                CheckItem:
                    text: "Daily"
                    group: "child"

                CheckItem:
                    text: "Weekly"
                    group: "child"

                CheckItem:
                    text: "Monthly"
                    group: "child"

        MDWidget:
    '''


    class CheckItem(MDBoxLayout):
        text = StringProperty()
        group = StringProperty()


    class Example(MDApp):
        def build(self):
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette = "Teal"
            return Builder.load_string(KV)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/checkbox-parent-child.gif
    :align: center

.. MDSwitch:
MDSwitch
--------

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/switch.png
    :align: center

Usage
-----

.. code-block:: python

    from kivy.lang import Builder

    from kivymd.app import MDApp

    KV = '''
    MDFloatLayout:

        MDSwitch:
            pos_hint: {'center_x': .5, 'center_y': .5}
    '''


    class Example(MDApp):
        def build(self):
            self.theme_cls.primary_palette = "Green"
            self.theme_cls.theme_style = "Dark"
            return Builder.load_string(KV)


    Example().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/md-switch.gif
    :align: center

.. Note:: Control state of :class:`~MDSwitch` same way as in
    :class:`~MDCheckbox`.
"""
__all__ = ("MDCheckbox", "MDSwitch")
class MDCheckbox(CircularRippleBehavior, ScaleBehavior, ToggleButtonBehavior, MDIcon):
    """
    Checkbox class.

    For more information, see in the
    :class:`~kivymd.uix.behaviors.CircularRippleBehavior` and
    :class:`~kivy.uix.behaviors.ToggleButtonBehavior` and
    :class:`~kivymd.uix.label.MDIcon`
    classes documentation.
    """
    __allow_child_checkboxes_active = ...
    __allow_root_checkbox_active = ...
    active = ...
    checkbox_icon_normal = ...
    checkbox_icon_down = ...
    radio_icon_normal = ...
    radio_icon_down = ...
    color_active = ...
    color_inactive = ...
    disabled_color = ...
    selected_color = ...
    unselected_color = ...
    _current_color = ...
    def __init__(self, **kwargs) -> None:
        ...
    
    def update_primary_color(self, instance, value) -> None:
        """
        Called when the values of
        :attr:`kivymd.theming.ThemableBehavior.theme_cls.theme_style` and
        :attr:`kivymd.theming.ThemableBehavior.theme_cls.primary_color`
        change.
        """
        ...
    
    def update_icon(self, *args) -> None:
        """
        Called when the values of
        :attr:`checkbox_icon_normal` and
        :attr:`checkbox_icon_down` and
        :attr:`radio_icon_normal` and
        :attr:`group`
        change.
        """
        ...
    
    def update_color(self, *args) -> None:
        """
        Called when the values of
        :attr:`color_active` and
        :attr:`color_inactive` and
        :attr:`disabled_color` and
        :attr:`disabled` and
        :attr:`state`
        change.
        """
        ...
    
    def on_state(self, *args) -> None:
        """Called when the values of :attr:`state` change."""
        ...
    
    def on_active(self, *args) -> None:
        """Called when the values of :attr:`active` change."""
        ...
    
    def set_root_active(self) -> None:
        ...
    
    def set_child_active(self, active: bool): # -> None:
        ...
    
    def on_touch_down(self, touch):
        ...
    


class ThumbIcon(MDIcon):
    """
    Implements icon for the :class:`~Thumb` widget.

    .. versionadded:: 1.0.0
    """
    ...


class Thumb(CommonElevationBehavior, CircularRippleBehavior, MDFloatLayout):
    """Implements a thumb for the :class:`~MDSwitch` widget."""
    ...


class MDSwitch(ThemableBehavior, FloatLayout):
    """
    Switch class.

    For more information, see in the
    :class:`~kivymd.theming.ThemableBehavior` and
    :class:`~kivy.uix.floatlayout.FloatLayout` classes documentation.
    """
    active = ...
    icon_active = ...
    icon_inactive = ...
    icon_active_color = ...
    icon_inactive_color = ...
    thumb_color_active = ...
    thumb_color_inactive = ...
    thumb_color_disabled = ...
    track_color_active = ...
    track_color_inactive = ...
    track_color_disabled = ...
    _thumb_pos = ...
    def __init__(self, **kwargs) -> None:
        ...
    
    def set_icon(self, instance_switch, icon_value: str) -> None:
        """
        Called when the values of
        :attr:`icon_active` and :attr:`icon_inactive` change.
        """
        ...
    
    def on_active(self, instance_switch, active_value: bool) -> None:
        """Called when the values of :attr:`active` change."""
        ...
    
    def on_thumb_down(self) -> None:
        """
        Called at the on_touch_down event of the :class:`~Thumb` object.
        Indicates the state of the switch "on/off" by an animation of
        increasing the size of the thumb.
        """
        ...
    


