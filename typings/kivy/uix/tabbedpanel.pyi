"""
This type stub file was generated by pyright.
"""

from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout

'''
TabbedPanel
===========

.. image:: images/tabbed_panel.jpg
    :align: right

.. versionadded:: 1.3.0


The `TabbedPanel` widget manages different widgets in tabs, with a header area
for the actual tab buttons and a content area for showing the current tab
content.

The :class:`TabbedPanel` provides one default tab.

Simple example
--------------

.. include:: ../../examples/widgets/tabbedpanel.py
    :literal:

.. note::

    A new class :class:`TabbedPanelItem` has been introduced in 1.5.0 for
    convenience. So now one can simply add a :class:`TabbedPanelItem` to a
    :class:`TabbedPanel` and `content` to the :class:`TabbedPanelItem`
    as in the example provided above.

Customize the Tabbed Panel
--------------------------

You can choose the position in which the tabs are displayed::

    tab_pos = 'top_mid'

An individual tab is called a TabbedPanelHeader. It is a special button
containing a `content` property. You add the TabbedPanelHeader first, and set
its `content` property separately::

    tp = TabbedPanel()
    th = TabbedPanelHeader(text='Tab2')
    tp.add_widget(th)

An individual tab, represented by a TabbedPanelHeader, needs its content set.
This content can be any widget. It could be a layout with a deep
hierarchy of widgets, or it could be an individual widget, such as a label or a
button::

    th.content = your_content_instance

There is one "shared" main content area active at any given time, for all
the tabs. Your app is responsible for adding the content of individual tabs
and for managing them, but it's not responsible for content switching. The
tabbed panel handles switching of the main content object as per user action.

There is a default tab added when the tabbed panel is instantiated.
Tabs that you add individually as above, are added in addition to the default
tab. Thus, depending on your needs and design, you will want to customize the
default tab::

    tp.default_tab_text = 'Something Specific To Your Use'


The default tab machinery requires special consideration and management.
Accordingly, an `on_default_tab` event is provided for associating a callback::

    tp.bind(default_tab = my_default_tab_callback)

It's important to note that by default, :attr:`default_tab_cls` is of type
:class:`TabbedPanelHeader` and thus has the same properties as other tabs.

Since 1.5.0, it is now possible to disable the creation of the
:attr:`default_tab` by setting :attr:`do_default_tab` to False.

Tabs and content can be removed in several ways::

    tp.remove_widget(widget/tabbed_panel_header)
    or
    tp.clear_widgets() # to clear all the widgets in the content area
    or
    tp.clear_tabs() # to remove the TabbedPanelHeaders

To access the children of the tabbed panel, use content.children::

    tp.content.children

To access the list of tabs::

    tp.tab_list

To change the appearance of the main tabbed panel content::

    background_color = (1, 0, 0, .5) #50% translucent red
    border = [0, 0, 0, 0]
    background_image = 'path/to/background/image'

To change the background of a individual tab, use these two properties::

    tab_header_instance.background_normal = 'path/to/tab_head/img'
    tab_header_instance.background_down = 'path/to/tab_head/img_pressed'

A TabbedPanelStrip contains the individual tab headers. To change the
appearance of this tab strip, override the canvas of TabbedPanelStrip.
For example, in the kv language:

.. code-block:: kv

    <TabbedPanelStrip>
        canvas:
            Color:
                rgba: (0, 1, 0, 1) # green
            Rectangle:
                size: self.size
                pos: self.pos

By default the tabbed panel strip takes its background image and color from the
tabbed panel's background_image and background_color.

'''
__all__ = ('StripLayout', 'TabbedPanel', 'TabbedPanelContent', 'TabbedPanelHeader', 'TabbedPanelItem', 'TabbedPanelStrip', 'TabbedPanelException')
class TabbedPanelException(Exception):
    '''The TabbedPanelException class.
    '''
    ...


class TabbedPanelHeader(ToggleButton):
    '''A Base for implementing a Tabbed Panel Head. A button intended to be
    used as a Heading/Tab for a TabbedPanel widget.

    You can use this TabbedPanelHeader widget to add a new tab to a
    TabbedPanel.
    '''
    content = ...
    def on_touch_down(self, touch): # -> None:
        ...
    
    def on_release(self, *largs): # -> None:
        ...
    


class TabbedPanelItem(TabbedPanelHeader):
    '''This is a convenience class that provides a header of type
    TabbedPanelHeader and links it with the content automatically. Thus
    facilitating you to simply do the following in kv language:

    .. code-block:: kv

        <TabbedPanel>:
            # ...other settings
            TabbedPanelItem:
                BoxLayout:
                    Label:
                        text: 'Second tab content area'
                    Button:
                        text: 'Button that does nothing'

    .. versionadded:: 1.5.0
    '''
    def add_widget(self, widget, *args, **kwargs): # -> None:
        ...
    
    def remove_widget(self, *args, **kwargs): # -> None:
        ...
    


class TabbedPanelStrip(GridLayout):
    '''A strip intended to be used as background for Heading/Tab.
    This does not cover the blank areas in case the tabs don't cover
    the entire width/height of the TabbedPanel(use :class:`StripLayout`
    for that).
    '''
    tabbed_panel = ...


class StripLayout(GridLayout):
    ''' The main layout that is used to house the entire tabbedpanel strip
    including the blank areas in case the tabs don't cover the entire
    width/height.

    .. versionadded:: 1.8.0

    '''
    border = ...
    background_image = ...


class TabbedPanelContent(FloatLayout):
    '''The TabbedPanelContent class.
    '''
    ...


class TabbedPanel(GridLayout):
    '''The TabbedPanel class. See module documentation for more information.
    '''
    background_color = ...
    border = ...
    background_image = ...
    background_disabled_image = ...
    strip_image = ...
    strip_border = ...
    _current_tab = ...
    def get_current_tab(self): # -> TabbedPanelHeader | _:
        ...
    
    current_tab = ...
    tab_pos = ...
    tab_height = ...
    tab_width = ...
    bar_width = ...
    scroll_type = ...
    do_default_tab = ...
    default_tab_text = ...
    default_tab_cls = ...
    def get_tab_list(self): # -> float:
        ...
    
    tab_list = ...
    content = ...
    _default_tab = ...
    def get_def_tab(self): # -> TabbedPanelHeader | _:
        ...
    
    def set_def_tab(self, new_tab): # -> None:
        ...
    
    default_tab = ...
    def get_def_tab_content(self):
        ...
    
    def set_def_tab_content(self, *l): # -> None:
        ...
    
    default_tab_content = ...
    _update_tabs_ev = ...
    def __init__(self, **kwargs) -> None:
        ...
    
    def switch_to(self, header, do_scroll=...): # -> None:
        '''Switch to a specific panel header.

        .. versionchanged:: 1.10.0

        If used with `do_scroll=True`, it scrolls
        to the header's tab too.

        :meth:`switch_to` cannot be called from within the
        :class:`TabbedPanel` or its subclass' ``__init__`` method.
        If that is required, use the ``Clock`` to schedule it. See `discussion
        <https://github.com/kivy/kivy/issues/3493#issuecomment-121567969>`_
        for full example.
        '''
        ...
    
    def clear_tabs(self, *l): # -> None:
        ...
    
    def add_widget(self, widget, *args, **kwargs): # -> None:
        ...
    
    def remove_widget(self, widget, *args, **kwargs): # -> None:
        ...
    
    def clear_widgets(self, *args, **kwargs): # -> None:
        ...
    
    def on_strip_image(self, instance, value): # -> None:
        ...
    
    def on_strip_border(self, instance, value): # -> None:
        ...
    
    def on_do_default_tab(self, instance, value): # -> None:
        ...
    
    def on_default_tab_text(self, *args): # -> None:
        ...
    
    def on_tab_width(self, *l): # -> None:
        ...
    
    def on_tab_height(self, *l): # -> None:
        ...
    
    def on_tab_pos(self, *l): # -> None:
        ...
    


