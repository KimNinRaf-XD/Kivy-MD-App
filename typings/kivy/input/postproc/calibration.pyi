"""
This type stub file was generated by pyright.
"""

'''
Calibration
===========

.. versionadded:: 1.9.0

Recalibrate input device to a specific range / offset.

Let's say you have 3 1080p displays, the 2 firsts are multitouch. By default,
both will have mixed touch, the range will conflict with each others: the 0-1
range will goes to 0-5760 px (remember, 3 * 1920 = 5760.)

To fix it, you need to manually reference them. For example::

    [input]
    left = mtdev,/dev/input/event17
    middle = mtdev,/dev/input/event15
    # the right screen is just a display.

Then, you can use the calibration postproc module::

    [postproc:calibration]
    left = xratio=0.3333
    middle = xratio=0.3333,xoffset=0.3333

Now, the touches from the left screen will be within 0-0.3333 range, and the
touches from the middle screen will be within 0.3333-0.6666 range.

You can also match calibration rules to devices based on their provider type.
This is useful when probesysfs is used to match devices. For example::

    [input]
    mtdev_%(name)s = probesysfs,provider=mtdev

Then to apply calibration to any mtdev device, you can assign rules to the
provider name enclosed by parentheses::

    [postproc:calibration]
    (mtdev) = xratio=0.3333,xoffset=0.3333

Calibrating devices like this means the device's path doesn't need to be
configured ahead of time. Note that with this method, all mtdev inputs will
have the same calibration applied to them. For this reason, matching by
provider will typically be useful when expecting only one input device.
'''
__all__ = ('InputPostprocCalibration', )
class InputPostprocCalibration:
    '''Recalibrate the inputs.

    The configuration must go within a section named `postproc:calibration`.
    Within the section, you must have a line like::

        devicename = param=value,param=value

    If you wish to match by provider, you must have a line like::

        (provider) = param=value,param=value

    :Parameters:
        `xratio`: float
            Value to multiply X
        `yratio`: float
            Value to multiply Y
        `xoffset`: float
            Value to add to X
        `yoffset`: float
            Value to add to Y
        `auto`: str
            If set, then the touch is transformed from screen-relative
            to window-relative The value is used as an indication of
            screen size, e.g for fullHD:

                auto=1920x1080

            If present, this setting overrides all the others.
            This assumes the input device exactly covers the display
            area, if they are different, the computations will be wrong.

    .. versionchanged:: 1.11.0
        Added `auto` parameter
    '''
    def __init__(self) -> None:
        ...
    
    def process(self, events):
        ...
    
    def auto_calibrate(self, sx, sy, size): # -> tuple[Unknown, Unknown]:
        ...
    

