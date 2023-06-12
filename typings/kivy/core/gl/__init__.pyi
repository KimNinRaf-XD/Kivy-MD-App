"""
This type stub file was generated by pyright.
"""

import sys
import kivy.core.window
from os import environ
from kivy.logger import Logger
from kivy.graphics import gl_init_resources
from kivy.graphics.opengl_utils import gl_get_version
from kivy.graphics.opengl import GL_MAX_TEXTURE_IMAGE_UNITS, GL_MAX_TEXTURE_SIZE, GL_RENDERER, GL_SHADING_LANGUAGE_VERSION, GL_VENDOR, GL_VERSION, glGetIntegerv, glGetString, gl_init_symbols
from kivy.graphics.cgl import cgl_get_initialized_backend_name
from kivy.utils import platform

'''
OpenGL
======

Select and use the best OpenGL library available. Depending on your system, the
core provider can select an OpenGL ES or a 'classic' desktop OpenGL library.
'''
MIN_REQUIRED_GL_VERSION = ...
def msgbox(message):
    ...

if 'KIVY_DOC' not in environ:
    def init_gl(allowed=..., ignored=...): # -> None:
        ...
    
    def print_gl_version(): # -> None:
        ...
    
