"""
This type stub file was generated by pyright.
"""

"""
Controllers/WindowController
============================

.. versionadded:: 1.0.0

Modules and classes that implement useful methods for getting information
about the state of the current application window.

Controlling the resizing direction of the application window
------------------------------------------------------------

.. code-block:: python

    # When resizing the application window, the direction of change will be
    # printed - 'left' or 'right'.

    from kivymd.app import MDApp
    from kivymd.uix.controllers import WindowController
    from kivymd.uix.screen import MDScreen


    class MyScreen(MDScreen, WindowController):
        def on_width(self, *args):
            print(self.get_window_width_resizing_direction())


    class Test(MDApp):
        def build(self):
            return MyScreen()


    Test().run()
"""
class WindowController:
    def __init__(self) -> None:
        ...
    
    def on_size(self, instance, size: list) -> None:
        """Called when the application screen size changes."""
        ...
    
    def get_real_device_type(self) -> str:
        """Returns the device type - 'mobile', 'tablet' or 'desktop'."""
        ...
    
    def get_window_width_resizing_direction(self) -> str:
        """Return window width resizing direction - 'left' or 'right'."""
        ...
    


