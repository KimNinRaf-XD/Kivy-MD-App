"""
This type stub file was generated by pyright.
"""

from kivy.uix.label import Label

"""
Monitor module
==============

The Monitor module is a toolbar that shows the activity of your current
application :

* FPS

"""
class FpsMonitor(Label):
    updated_interval = ...
    _fsp_value = ...
    def start(self): # -> None:
        ...
    
    def update_fps(self, *args): # -> None:
        ...
    


