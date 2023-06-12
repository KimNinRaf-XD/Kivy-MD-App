"""
This type stub file was generated by pyright.
"""

from kivy.app import App
from kivy.event import EventDispatcher
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout

'''Screen Manager
==============

.. image:: images/screenmanager.gif
    :align: right

.. versionadded:: 1.4.0

The screen manager is a widget dedicated to managing multiple screens for your
application. The default :class:`ScreenManager` displays only one
:class:`Screen` at a time and uses a :class:`TransitionBase` to switch from one
Screen to another.

Multiple transitions are supported based on changing the screen coordinates /
scale or even performing fancy animation using custom shaders.

Basic Usage
-----------

Let's construct a Screen Manager with 4 named screens. When you are creating
a screen, **you absolutely need to give a name to it**::

    from kivy.uix.screenmanager import ScreenManager, Screen

    # Create the manager
    sm = ScreenManager()

    # Add few screens
    for i in range(4):
        screen = Screen(name='Title %d' % i)
        sm.add_widget(screen)

    # By default, the first screen added into the ScreenManager will be
    # displayed. You can then change to another screen.

    # Let's display the screen named 'Title 2'
    # A transition will automatically be used.
    sm.current = 'Title 2'

The default :attr:`ScreenManager.transition` is a :class:`SlideTransition` with
options :attr:`~SlideTransition.direction` and
:attr:`~TransitionBase.duration`.

Please note that by default, a :class:`Screen` displays nothing: it's just a
:class:`~kivy.uix.relativelayout.RelativeLayout`. You need to use that class as
a root widget for your own screen, the best way being to subclass.

.. warning::
    As :class:`Screen` is a :class:`~kivy.uix.relativelayout.RelativeLayout`,
    it is important to understand the
    :ref:`kivy-uix-relativelayout-common-pitfalls`.

Here is an example with a 'Menu Screen' and a 'Settings Screen'::

    from kivy.app import App
    from kivy.lang import Builder
    from kivy.uix.screenmanager import ScreenManager, Screen

    # Create both screens. Please note the root.manager.current: this is how
    # you can control the ScreenManager from kv. Each screen has by default a
    # property manager that gives you the instance of the ScreenManager used.
    Builder.load_string("""
    <MenuScreen>:
        BoxLayout:
            Button:
                text: 'Goto settings'
                on_press: root.manager.current = 'settings'
            Button:
                text: 'Quit'

    <SettingsScreen>:
        BoxLayout:
            Button:
                text: 'My settings button'
            Button:
                text: 'Back to menu'
                on_press: root.manager.current = 'menu'
    """)

    # Declare both screens
    class MenuScreen(Screen):
        pass

    class SettingsScreen(Screen):
        pass

    class TestApp(App):

        def build(self):
            # Create the screen manager
            sm = ScreenManager()
            sm.add_widget(MenuScreen(name='menu'))
            sm.add_widget(SettingsScreen(name='settings'))

            return sm

    if __name__ == '__main__':
        TestApp().run()


Changing Direction
------------------

A common use case for :class:`ScreenManager` involves using a
:class:`SlideTransition` which slides right to the next screen
and slides left to the previous screen. Building on the previous
example, this can be accomplished like so::

    Builder.load_string("""
    <MenuScreen>:
        BoxLayout:
            Button:
                text: 'Goto settings'
                on_press:
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'settings'
            Button:
                text: 'Quit'

    <SettingsScreen>:
        BoxLayout:
            Button:
                text: 'My settings button'
            Button:
                text: 'Back to menu'
                on_press:
                    root.manager.transition.direction = 'right'
                    root.manager.current = 'menu'
    """)


Advanced Usage
--------------

From 1.8.0, you can now switch dynamically to a new screen, change the
transition options and remove the previous one by using
:meth:`~ScreenManager.switch_to`::

    sm = ScreenManager()
    screens = [Screen(name='Title {}'.format(i)) for i in range(4)]

    sm.switch_to(screens[0])
    # later
    sm.switch_to(screens[1], direction='right')

Note that this method adds the screen to the :class:`ScreenManager` instance
and should not be used if your screens have already been added to this
instance. To switch to a screen which is already added, you should use the
:attr:`~ScreenManager.current` property.


Changing transitions
--------------------

You have multiple transitions available by default, such as:

- :class:`NoTransition` - switches screens instantly with no animation
- :class:`SlideTransition` - slide the screen in/out, from any direction
- :class:`CardTransition` - new screen slides on the previous
  or the old one slides off the new one depending on the mode
- :class:`SwapTransition` - implementation of the iOS swap transition
- :class:`FadeTransition` - shader to fade the screen in/out
- :class:`WipeTransition` - shader to wipe the screens from right to left
- :class:`FallOutTransition` - shader where the old screen 'falls' and
  becomes transparent, revealing the new one behind it.
- :class:`RiseInTransition` - shader where the new screen rises from the
  screen centre while fading from transparent to opaque.

You can easily switch transitions by changing the
:attr:`ScreenManager.transition` property::

    sm = ScreenManager(transition=FadeTransition())

.. note::

    Currently, none of Shader based Transitions use
    anti-aliasing. This is because they use the FBO which doesn't have
    any logic to handle supersampling. This is a known issue and we
    are working on a transparent implementation that will give the
    same results as if it had been rendered on screen.

    To be more concrete, if you see sharp edged text during the animation, it's
    normal.

'''
__all__ = (
    "Screen",
    "ScreenManager",
    "ScreenManagerException",
    "TransitionBase",
    "ShaderTransition",
    "SlideTransition",
    "SwapTransition",
    "FadeTransition",
    "WipeTransition",
    "FallOutTransition",
    "RiseInTransition",
    "NoTransition",
    "CardTransition",
)

class ScreenManagerException(Exception):
    """Exception for the :class:`ScreenManager`."""

    ...

class Screen(RelativeLayout):
    """Screen is an element intended to be used with a :class:`ScreenManager`.
    Check module documentation for more information.

    :Events:
        `on_pre_enter`: ()
            Event fired when the screen is about to be used: the entering
            animation is started.
        `on_enter`: ()
            Event fired when the screen is displayed: the entering animation is
            complete.
        `on_pre_leave`: ()
            Event fired when the screen is about to be removed: the leaving
            animation is started.
        `on_leave`: ()
            Event fired when the screen is removed: the leaving animation is
            finished.

    .. versionchanged:: 1.6.0
        Events `on_pre_enter`, `on_enter`, `on_pre_leave` and `on_leave` were
        added.
    """

    name = ...
    manager = ...
    transition_progress = ...
    transition_state = ...
    __events__ = ...
    def on_pre_enter(self, *args): ...
    def on_enter(self, *args): ...
    def on_pre_leave(self, *args): ...
    def on_leave(self, *args): ...
    def __repr__(self): ...

class TransitionBase(EventDispatcher):
    """TransitionBase is used to animate 2 screens within the
    :class:`ScreenManager`. This class acts as a base for other
    implementations like the :class:`SlideTransition` and
    :class:`SwapTransition`.

    :Events:
        `on_progress`: Transition object, progression float
            Fired during the animation of the transition.
        `on_complete`: Transition object
            Fired when the transition is finished.
    """

    screen_out = ...
    screen_in = ...
    duration = ...
    manager = ...
    is_active = ...
    _anim = ...
    __events__ = ...
    def start(self, manager):  # -> None:
        """(internal) Starts the transition. This is automatically
        called by the :class:`ScreenManager`.
        """
        ...
    def stop(self):  # -> None:
        """(internal) Stops the transition. This is automatically called by the
        :class:`ScreenManager`.
        """
        ...
    def add_screen(self, screen):  # -> None:
        """(internal) Used to add a screen to the :class:`ScreenManager`."""
        ...
    def remove_screen(self, screen):  # -> None:
        """(internal) Used to remove a screen from the :class:`ScreenManager`."""
        ...
    def on_complete(self): ...
    def on_progress(self, progression): ...

class ShaderTransition(TransitionBase):
    '''Transition class that uses a Shader for animating the transition between
    2 screens. By default, this class doesn't assign any fragment/vertex
    shader. If you want to create your own fragment shader for the transition,
    you need to declare the header yourself and include the "t", "tex_in" and
    "tex_out" uniform::

        # Create your own transition. This shader implements a "fading"
        # transition.
        fs = """$HEADER
            uniform float t;
            uniform sampler2D tex_in;
            uniform sampler2D tex_out;

            void main(void) {
                vec4 cin = texture2D(tex_in, tex_coord0);
                vec4 cout = texture2D(tex_out, tex_coord0);
                gl_FragColor = mix(cout, cin, t);
            }
        """

        # And create your transition
        tr = ShaderTransition(fs=fs)
        sm = ScreenManager(transition=tr)

    '''

    fs = ...
    vs = ...
    clearcolor = ...
    def make_screen_fbo(self, screen): ...
    def on_progress(self, progress): ...
    def on_complete(self): ...
    def add_screen(self, screen): ...
    def remove_screen(self, screen): ...
    def stop(self): ...

class NoTransition(TransitionBase):
    """No transition, instantly switches to the next screen with no delay or
    animation.

    .. versionadded:: 1.8.0
    """

    duration = ...
    def on_complete(self): ...

class SlideTransition(TransitionBase):
    """Slide Transition, can be used to show a new screen from any direction:
    left, right, up or down.
    """

    direction = ...
    def on_progress(self, progression): ...
    def on_complete(self): ...

class CardTransition(SlideTransition):
    """Card transition that looks similar to Android 4.x application drawer
    interface animation.

    It supports 4 directions like SlideTransition: left, right, up and down,
    and two modes, pop and push. If push mode is activated, the previous
    screen does not move, and the new one slides in from the given direction.
    If the pop mode is activated, the previous screen slides out, when the new
    screen is already on the position of the ScreenManager.

    .. versionadded:: 1.10
    """

    mode = ...
    def start(self, manager):  # -> None:
        """(internal) Starts the transition. This is automatically
        called by the :class:`ScreenManager`.
        """
        ...
    def on_progress(self, progression): ...

class SwapTransition(TransitionBase):
    """Swap transition that looks like iOS transition when a new window
    appears on the screen.
    """

    def __init__(self, **kwargs) -> None: ...
    def start(self, manager): ...
    def update_scale(self, screen, center): ...
    def add_screen(self, screen): ...
    def on_complete(self): ...
    def on_progress(self, progression): ...

class WipeTransition(ShaderTransition):
    """Wipe transition, based on a fragment Shader."""

    WIPE_TRANSITION_FS = ...
    fs = ...

class FadeTransition(ShaderTransition):
    """Fade transition, based on a fragment Shader."""

    FADE_TRANSITION_FS = ...
    fs = ...

class FallOutTransition(ShaderTransition):
    """Transition where the new screen 'falls' from the screen centre,
    becoming smaller and more transparent until it disappears, and
    revealing the new screen behind it. Mimics the popular/standard
    Android transition.

    .. versionadded:: 1.8.0

    """

    duration = ...
    FALLOUT_TRANSITION_FS = ...
    fs = ...

class RiseInTransition(ShaderTransition):
    """Transition where the new screen rises from the screen centre,
    becoming larger and changing from transparent to opaque until it
    fills the screen. Mimics the popular/standard Android transition.

    .. versionadded:: 1.8.0
    """

    duration = ...
    RISEIN_TRANSITION_FS = ...
    fs = ...

class ScreenManager(FloatLayout):
    """Screen manager. This is the main class that will control your
    :class:`Screen` stack and memory.

    By default, the manager will show only one screen at a time.
    """

    current = ...
    transition = ...
    screens = ...
    current_screen = ...
    screen_names = ...
    def __init__(self, **kwargs) -> None: ...
    def add_widget(self, widget, *args, **kwargs):  # -> None:
        """
        .. versionchanged:: 2.1.0
            Renamed argument `screen` to `widget`.
        """
        ...
    def remove_widget(self, widget, *args, **kwargs): ...
    def clear_widgets(self, children=..., *args, **kwargs):  # -> None:
        """
        .. versionchanged:: 2.1.0
            Renamed argument `screens` to `children`.
        """
        ...
    def real_add_widget(self, screen, *args): ...
    def real_remove_widget(self, screen, *args): ...
    def on_current(self, instance, value): ...
    def get_screen(self, name):
        """Return the screen widget associated with the name or raise a
        :class:`ScreenManagerException` if not found.
        """
        ...
    def has_screen(self, name):  # -> bool:
        """Return True if a screen with the `name` has been found.

        .. versionadded:: 1.6.0
        """
        ...
    def __next__(self):  # -> None:
        """Py2K backwards compatibility without six or other lib."""
        ...
    def next(self):  # -> None:
        """Return the name of the next screen from the screen list."""
        ...
    def previous(self):  # -> None:
        """Return the name of the previous screen from the screen list."""
        ...
    def switch_to(self, screen, **options):  # -> None:
        """Add a new or existing screen to the ScreenManager and switch to it.
        The previous screen will be "switched away" from. `options` are the
        :attr:`transition` options that will be changed before the animation
        happens.

        If no previous screens are available, the screen will be used as the
        main one::

            sm = ScreenManager()
            sm.switch_to(screen1)
            # later
            sm.switch_to(screen2, direction='left')
            # later
            sm.switch_to(screen3, direction='right', duration=1.)

        If any animation is in progress, it will be stopped and replaced by
        this one: you should avoid this because the animation will just look
        weird. Use either :meth:`switch_to` or :attr:`current` but not both.

        The `screen` name will be changed if there is any conflict with the
        current screen.

        .. versionadded: 1.8.0
        """
        ...
    def on_motion(self, etype, me): ...
    def on_touch_down(self, touch): ...
    def on_touch_move(self, touch): ...
    def on_touch_up(self, touch): ...

if __name__ == "__main__":
    class TestApp(App):
        def change_view(self, *l): ...
        def remove_screen(self, *l): ...
        def build(self): ...
