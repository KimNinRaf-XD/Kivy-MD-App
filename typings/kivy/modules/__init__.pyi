"""
This type stub file was generated by pyright.
"""

import importlib
import os
import sys

import kivy
from kivy.config import Config
from kivy.logger import Logger

"""
Modules
=======

Modules are classes that can be loaded when a Kivy application is starting. The
loading of modules is managed by the config file. Currently, we include:

    * :class:`~kivy.modules.touchring`: Draw a circle around each touch.
    * :class:`~kivy.modules.monitor`: Add a red topbar that indicates the FPS
      and a small graph indicating input activity.
    * :class:`~kivy.modules.keybinding`: Bind some keys to actions, such as a
      screenshot.
    * :class:`~kivy.modules.recorder`: Record and playback a sequence of
      events.
    * :class:`~kivy.modules.screen`: Emulate the characteristics (dpi/density/
      resolution) of different screens.
    * :class:`~kivy.modules.inspector`: Examines your widget hierarchy and
      widget properties.
    * :class:`~kivy.modules.webdebugger`: Realtime examination of your app
      internals via a web browser.
    * :class:`~kivy.modules.joycursor`: Navigate in your app with a joystick.
    * :class:`~kivy.modules.showborder`: Show widget's border.

Modules are automatically loaded from the Kivy path and User path:

    * `PATH_TO_KIVY/kivy/modules`
    * `HOME/.kivy/mods`

Activating a module
-------------------

There are various ways in which you can activate a kivy module.

Activate a module in the config
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To activate a module this way, you can edit your configuration file (in your
`HOME/.kivy/config.ini`)::

    [modules]
    # uncomment to activate
    touchring =
    # monitor =
    # keybinding =

Only the name of the module followed by "=" is sufficient to activate the
module.

Activate a module in Python
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Before starting your application, preferably at the start of your import, you
can do something like this::

    import kivy
    kivy.require('1.0.8')

    # Activate the touchring module
    from kivy.config import Config
    Config.set('modules', 'touchring', '')

Activate a module via the commandline
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When starting your application from the commandline, you can add a
*-m <modulename>* to the arguments. For example::

    python main.py -m webdebugger

.. note::
    Some modules, such as the screen, may require additional parameters. They
    will, however, print these parameters to the console when launched without
    them.


Create your own module
----------------------

Create a file in your `HOME/.kivy/mods`, and create 2 functions::

    def start(win, ctx):
        pass

    def stop(win, ctx):
        pass

Start/stop are functions that will be called for every window opened in
Kivy. When you are starting a module, you can use these to store and
manage the module state. Use the `ctx` variable as a dictionary. This
context is unique for each instance/start() call of the module, and will
be passed to stop() too.

"""
__all__ = ("Modules",)

class ModuleContext:
    """Context of a module

    You can access to the config with self.config.
    """

    def __init__(self) -> None: ...
    def __repr__(self): ...

class ModuleBase:
    """Handle Kivy modules. It will automatically load and instantiate the
    module for the general window."""

    def __init__(self, **kwargs) -> None: ...
    def add_path(self, path):  # -> None:
        """Add a path to search for modules in"""
        ...
    def list(self):  # -> dict[Unknown, Unknown]:
        """Return the list of available modules"""
        ...
    def import_module(self, name): ...
    def activate_module(self, name, win):  # -> None:
        """Activate a module on a window"""
        ...
    def deactivate_module(self, name, win):  # -> None:
        """Deactivate a module from a window"""
        ...
    def register_window(self, win):  # -> None:
        """Add the window to the window list"""
        ...
    def unregister_window(self, win):  # -> None:
        """Remove the window from the window list"""
        ...
    def update(self):  # -> None:
        """Update the status of the module for each window"""
        ...
    def configure(self):  # -> None:
        """(internal) Configure all the modules before using them."""
        ...
    def usage_list(self): ...

Modules = ...
if "KIVY_DOC" not in os.environ: ...
if __name__ == "__main__": ...
