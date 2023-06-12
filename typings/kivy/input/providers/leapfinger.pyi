"""
This type stub file was generated by pyright.
"""

from kivy.input.motionevent import MotionEvent
from kivy.input.provider import MotionEventProvider

"""
Leap Motion - finger only
=========================
"""
__all__ = ("LeapFingerEventProvider", "LeapFingerEvent")
_LEAP_QUEUE = ...
InteractionBox = ...

def normalize(value, a, b): ...

class LeapFingerEvent(MotionEvent):
    def __init__(self, *args, **kwargs) -> None: ...
    def depack(self, args): ...

class LeapFingerEventProvider(MotionEventProvider):
    __handlers__ = ...
    def start(self):  # -> None:
        class LeapMotionListener(Leap.Listener): ...

    def update(self, dispatch_fn): ...
    def process_frame(self, frame): ...
