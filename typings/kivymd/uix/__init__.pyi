"""
This type stub file was generated by pyright.
"""

from kivy.properties import BooleanProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivymd.uix.behaviors import SpecificBackgroundColorBehavior

__all__ = ("MDAdaptiveWidget", )
class MDAdaptiveWidget(SpecificBackgroundColorBehavior):
    adaptive_height = ...
    adaptive_width = ...
    adaptive_size = ...
    def on_adaptive_height(self, md_widget, value: bool) -> None:
        ...
    
    def on_adaptive_width(self, md_widget, value: bool) -> None:
        ...
    
    def on_adaptive_size(self, md_widget, value: bool) -> None:
        ...
    

