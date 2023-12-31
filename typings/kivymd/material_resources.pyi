"""
This type stub file was generated by pyright.
"""

import os
from kivy.metrics import dp
from kivy.utils import platform

"""
Material Resources
==================
"""
if "KIVY_DOC_INCLUDE" in os.environ:
    dp = ...
DEVICE_IOS = platform == "ios" or platform == "macosx"
if platform != "android" and platform != "ios":
    DEVICE_TYPE = ...
else:
    DEVICE_TYPE = ...
    DEVICE_TYPE = ...
if DEVICE_TYPE == "mobile":
    MAX_NAV_DRAWER_WIDTH = ...
    HORIZ_MARGINS = ...
    STANDARD_INCREMENT = ...
    PORTRAIT_TOOLBAR_HEIGHT = ...
    LANDSCAPE_TOOLBAR_HEIGHT = ...
else:
    MAX_NAV_DRAWER_WIDTH = ...
    HORIZ_MARGINS = ...
    STANDARD_INCREMENT = ...
    PORTRAIT_TOOLBAR_HEIGHT = ...
    LANDSCAPE_TOOLBAR_HEIGHT = ...
TOUCH_TARGET_HEIGHT = ...
