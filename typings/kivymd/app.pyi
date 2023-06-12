"""
This type stub file was generated by pyright.
"""

from typing import Any

from kivy.app import App

"""
Themes/Material App
===================

This module contains :class:`MDApp` class that is inherited from
:class:`~kivy.app.App`. :class:`MDApp` has some properties needed for ``KivyMD``
library (like :attr:`~MDApp.theme_cls`). You can turn on the monitor displaying
the current ``FPS`` value in your application:

.. code-block:: python

    KV = '''
    MDScreen:

        MDLabel:
            text: "Hello, World!"
            halign: "center"
    '''

    from kivy.lang import Builder

    from kivymd.app import MDApp


    class MainApp(MDApp):
        def build(self):
            return Builder.load_string(KV)

        def on_start(self):
            self.fps_monitor_start()


    MainApp().run()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/fps-monitor.png
    :width: 350 px
    :align: center

"""
__all__ = ("MDApp",)

class FpsMonitoring:
    """Implements a monitor to display the current FPS in the toolbar."""

    def fps_monitor_start(self) -> None:
        """Adds a monitor to the main application window."""
        ...

class MDApp(App, FpsMonitoring):
    """
    Application class, see :class:`~kivy.app.App` class documentation for more
    information.
    """

    root = ...
    icon = ...
    theme_cls = ...
    def __init__(self, **kwargs: Any) -> None: ...
    def load_all_kv_files(self, path_to_directory: str) -> None:
        """
        Recursively loads KV files from the selected directory.

        .. versionadded:: 1.0.0
        """
        ...