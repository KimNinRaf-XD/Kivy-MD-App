"""
This type stub file was generated by pyright.
"""

'''
Motion Event Provider
=====================

Abstract class for the implementation of a
:class:`~kivy.input.motionevent.MotionEvent`
provider. The implementation must support the
:meth:`~MotionEventProvider.start`, :meth:`~MotionEventProvider.stop` and
:meth:`~MotionEventProvider.update` methods.
'''
__all__ = ('MotionEventProvider', )
class MotionEventProvider:
    '''Base class for a provider.
    '''
    def __init__(self, device, args) -> None:
        ...
    
    def start(self): # -> None:
        '''Start the provider. This method is automatically called when the
        application is started and if the configuration uses the current
        provider.
        '''
        ...
    
    def stop(self): # -> None:
        '''Stop the provider.
        '''
        ...
    
    def update(self, dispatch_fn): # -> None:
        '''Update the provider and dispatch all the new touch events though the
        `dispatch_fn` argument.
        '''
        ...
    


