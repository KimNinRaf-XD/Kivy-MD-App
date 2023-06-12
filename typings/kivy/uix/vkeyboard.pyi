"""
This type stub file was generated by pyright.
"""

from kivy.uix.scatter import Scatter

"""
VKeyboard
=========

.. image:: images/vkeyboard.jpg
    :align: right

.. versionadded:: 1.0.8


VKeyboard is an onscreen keyboard for Kivy. Its operation is intended to be
transparent to the user. Using the widget directly is NOT recommended. Read the
section `Request keyboard`_ first.

Modes
-----

This virtual keyboard has a docked and free mode:

* docked mode (:attr:`VKeyboard.docked` = True)
  Generally used when only one person is using the computer, like a tablet or
  personal computer etc.
* free mode: (:attr:`VKeyboard.docked` = False)
  Mostly for multitouch surfaces. This mode allows multiple virtual
  keyboards to be used on the screen.

If the docked mode changes, you need to manually call
:meth:`VKeyboard.setup_mode` otherwise the change will have no impact.
During that call, the VKeyboard, implemented on top of a
:class:`~kivy.uix.scatter.Scatter`, will change the
behavior of the scatter and position the keyboard near the target (if target
and docked mode is set).


Layouts
-------

The virtual keyboard is able to load a custom layout. If you create a new
layout and put the JSON in :file:`<kivy_data_dir>/keyboards/<layoutid>.json`,
you can load it by setting :attr:`VKeyboard.layout` to your layoutid.

The JSON must be structured like this::

    {
        "title": "Title of your layout",
        "description": "Description of your layout",
        "cols": 15,
        "rows": 5,

        ...
    }

Then, you need to describe the keys in each row, for either a "normal",
"shift" or a "special" (added in version 1.9.0) mode. Keys for this row
data must be named `normal_<row>`, `shift_<row>` and `special_<row>`.
Replace `row` with the row number.
Inside each row, you will describe the key. A key is a 4 element list in
the format::

    [ <text displayed on the keyboard>, <text to put when the key is pressed>,
      <text that represents the keycode>, <size of cols> ]

Here are example keys::

    # f key
    ["f", "f", "f", 1]
    # capslock
    ["\u21B9", "\t", "tab", 1.5]

Finally, complete the JSON::

    {
        ...
        "normal_1": [
            ["`", "`", "`", 1],    ["1", "1", "1", 1],    ["2", "2", "2", 1],
            ["3", "3", "3", 1],    ["4", "4", "4", 1],    ["5", "5", "5", 1],
            ["6", "6", "6", 1],    ["7", "7", "7", 1],    ["8", "8", "8", 1],
            ["9", "9", "9", 1],    ["0", "0", "0", 1],    ["+", "+", "+", 1],
            ["=", "=", "=", 1],    ["\u232b", null, "backspace", 2]
        ],

        "shift_1": [ ... ],
        "normal_2": [ ... ],
        "special_2": [ ... ],
        ...
    }


Request Keyboard
----------------

The instantiation of the virtual keyboard is controlled by the configuration.
Check `keyboard_mode` and `keyboard_layout` in the :doc:`api-kivy.config`.

If you intend to create a widget that requires a keyboard, do not use the
virtual keyboard directly, but prefer to use the best method available on
the platform. Check the :meth:`~kivy.core.window.WindowBase.request_keyboard`
method in the :doc:`api-kivy.core.window`.

If you want a specific layout when you request the keyboard, you should write
something like this (from 1.8.0, numeric.json can be in the same directory as
your main.py)::

    keyboard = Window.request_keyboard(
        self._keyboard_close, self)
    if keyboard.widget:
        vkeyboard = self._keyboard.widget
        vkeyboard.layout = 'numeric.json'

"""
__all__ = ("VKeyboard",)
default_layout_path = ...

class VKeyboard(Scatter):
    """
    VKeyboard is an onscreen keyboard with multitouch support.
    Its layout is entirely customizable and you can switch between available
    layouts using a button in the bottom right of the widget.

    :Events:
        `on_key_down`: keycode, internal, modifiers
            Fired when the keyboard received a key down event (key press).
        `on_key_up`: keycode, internal, modifiers
            Fired when the keyboard received a key up event (key release).
    """

    target = ...
    callback = ...
    layout = ...
    layout_path = ...
    available_layouts = ...
    docked = ...
    margin_hint = ...
    key_margin = ...
    font_size = ...
    background_color = ...
    background = ...
    background_disabled = ...
    key_background_color = ...
    key_background_normal = ...
    key_disabled_background_normal = ...
    key_background_down = ...
    background_border = ...
    key_border = ...
    layout_mode = ...
    layout_geometry = ...
    have_capslock = ...
    have_shift = ...
    have_special = ...
    active_keys = ...
    font_name = ...
    repeat_touch = ...
    _start_repeat_key_ev = ...
    _repeat_key_ev = ...
    __events__ = ...
    def __init__(self, **kwargs) -> None: ...
    def on_disabled(self, instance, value): ...
    def setup_mode(self, *largs):  # -> None:
        """Call this method when you want to readjust the keyboard according to
        options: :attr:`docked` or not, with attached :attr:`target` or not:

        * If :attr:`docked` is True, it will call :meth:`setup_mode_dock`
        * If :attr:`docked` is False, it will call :meth:`setup_mode_free`

        Feel free to overload these methods to create new
        positioning behavior.
        """
        ...
    def setup_mode_dock(self, *largs):  # -> None:
        """Setup the keyboard in docked mode.

        Dock mode will reset the rotation, disable translation, rotation and
        scale. Scale and position will be automatically adjusted to attach the
        keyboard to the bottom of the screen.

        .. note::
            Don't call this method directly, use :meth:`setup_mode` instead.
        """
        ...
    def setup_mode_free(self):  # -> None:
        """Setup the keyboard in free mode.

        Free mode is designed to let the user control the position and
        orientation of the keyboard. The only real usage is for a multiuser
        environment, but you might found other ways to use it.
        If a :attr:`target` is set, it will place the vkeyboard under the
        target.

        .. note::
            Don't call this method directly, use :meth:`setup_mode` instead.
        """
        ...
    def change_layout(self): ...
    def refresh(self, force=...):  # -> None:
        """(internal) Recreate the entire widget and graphics according to the
        selected layout.
        """
        ...
    def refresh_active_keys_layer(self): ...
    def refresh_keys_hint(self): ...
    def refresh_keys(self): ...
    def draw_keys(self): ...
    def on_key_down(self, *largs): ...
    def on_key_up(self, *largs): ...
    def on_textinput(self, *largs): ...
    def get_key_at_pos(self, x, y): ...
    def collide_margin(self, x, y):  # -> bool:
        """Do a collision test, and return True if the (x, y) is inside the
        vkeyboard margin.
        """
        ...
    def process_key_on(self, touch): ...
    def process_key_up(self, touch): ...
    def on_touch_down(self, touch): ...
    def on_touch_up(self, touch): ...

if __name__ == "__main__":
    vk = ...
