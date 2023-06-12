"""
This type stub file was generated by pyright.
"""

from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label

"""
Button
======

.. image:: images/button.jpg
    :align: right

The :class:`Button` is a :class:`~kivy.uix.label.Label` with associated actions
that are triggered when the button is pressed (or released after a
click/touch). To configure the button, the same properties (padding,
font_size, etc) and
:ref:`sizing system <kivy-uix-label-sizing-and-text-content>`
are used as for the :class:`~kivy.uix.label.Label` class::

    button = Button(text='Hello world', font_size=14)

To attach a callback when the button is pressed (clicked/touched), use
:class:`~kivy.uix.widget.Widget.bind`::

    def callback(instance):
        print('The button <%s> is being pressed' % instance.text)

    btn1 = Button(text='Hello world 1')
    btn1.bind(on_press=callback)
    btn2 = Button(text='Hello world 2')
    btn2.bind(on_press=callback)

If you want to be notified every time the button state changes, you can bind
to the :attr:`Button.state` property::

    def callback(instance, value):
        print('My button <%s> state is <%s>' % (instance, value))
    btn1 = Button(text='Hello world 1')
    btn1.bind(state=callback)

Kv Example::

    Button:
        text: 'press me'
        on_press: print("ouch! More gently please")
        on_release: print("ahhh")
        on_state:
            print("my current state is {}".format(self.state))

"""
__all__ = ("Button",)

class Button(ButtonBehavior, Label):
    """Button class, see module documentation for more information.

    .. versionchanged:: 1.8.0
        The behavior / logic of the button has been moved to
        :class:`~kivy.uix.behaviors.ButtonBehaviors`.

    """

    background_color = ...
    background_normal = ...
    background_down = ...
    background_disabled_normal = ...
    background_disabled_down = ...
    border = ...
