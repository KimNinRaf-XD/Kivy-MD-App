"""
This type stub file was generated by pyright.
"""

from ConfigParser import ConfigParser as PythonConfigParser
from os import environ

'''
Configuration object
====================

The :class:`Config` object is an instance of a modified Python ConfigParser.
See the `ConfigParser documentation
<http://docs.python.org/library/configparser.html>`_ for more information.

Kivy has a configuration file which determines the default settings. In
order to change these settings, you can alter this file manually or use
the Config object. Please see the :ref:`Configure Kivy` section for more
information.

Applying configurations
-----------------------

Configuration options control the initialization of the :class:`~kivy.app.App`.
In order to avoid situations where the config settings do not work or are not
applied before window creation (like setting an initial window size),
:meth:`Config.set <kivy.config.ConfigParser.set>` should be used before
importing any other Kivy modules. Ideally, this means setting them right at
the start of your main.py script.

Alternatively, you can save these settings permanently using
:meth:`Config.set <ConfigParser.set>` then
:meth:`Config.write <ConfigParser.write>`. In this case, you will need to
restart the app for the changes to take effect. Note that this approach will
effect all Kivy apps system wide.

Please note that no underscores (`_`) are allowed in the section name.

Usage of the Config object
--------------------------

To read a configuration token from a particular section::

    >>> from kivy.config import Config
    >>> Config.getint('kivy', 'show_fps')
    0

Change the configuration and save it::

    >>> Config.set('postproc', 'retain_time', '50')
    >>> Config.write()

For information on configuring your :class:`~kivy.app.App`, please see the
:ref:`Application configuration` section.

.. versionchanged:: 1.7.1
    The ConfigParser should work correctly with utf-8 now. The values are
    converted from ascii to unicode only when needed. The method get() returns
    utf-8 strings.

Changing configuration with environment variables
-------------------------------------------------

Since 1.11.0, it is now possible to change the configuration using
environment variables. They take precedence on the loaded config.ini.
The format is::

    KCFG_<section>_<key> = <value>

For example:

    KCFG_GRAPHICS_FULLSCREEN=auto ...
    KCFG_KIVY_LOG_LEVEL=warning ...

Or in your file before any kivy import:

    import os
    os.environ["KCFG_KIVY_LOG_LEVEL"] = "warning"

If you don't want to map any environment variables, you can disable
the behavior::

    os.environ["KIVY_NO_ENV_CONFIG"] = "1"


.. _configuration-tokens:

Available configuration tokens
------------------------------

.. |log_levels| replace::
    'trace', 'debug', 'info', 'warning', 'error' or 'critical'

:kivy:

    `default_font`: list
        Default fonts used for widgets displaying any text. It defaults to
        ['Roboto', 'data/fonts/Roboto-Regular.ttf',
        'data/fonts/Roboto-Italic.ttf', 'data/fonts/Roboto-Bold.ttf',
        'data/fonts/Roboto-BoldItalic.ttf'].
    `desktop`: int, 0 or 1
        This option controls desktop OS specific features, such as enabling
        drag-able scroll-bar in scroll views, disabling of bubbles in
        TextInput etc. 0 is disabled, 1 is enabled.
    `exit_on_escape`: int, 0 or 1
        Enables exiting kivy when escape is pressed.
        0 is disabled, 1 is enabled.
    `pause_on_minimize`: int, 0 or 1
        If set to `1`, the main loop is paused and the `on_pause` event
        is dispatched when the window is minimized. This option is intended
        for desktop use only. Defaults to `0`.
    `keyboard_layout`: string
        Identifier of the layout to use.
    `keyboard_mode`: string
        Specifies the keyboard mode to use. If can be one of the following:

        * '' - Let Kivy choose the best option for your current platform.
        * 'system' - real keyboard.
        * 'dock' - one virtual keyboard docked to a screen side.
        * 'multi' - one virtual keyboard for every widget request.
        * 'systemanddock' - virtual docked keyboard plus input from real
          keyboard.
        * 'systemandmulti' - analogous.
    `kivy_clock`: one of `default`, `interrupt`, `free_all`, `free_only`
        The clock type to use with kivy. See :mod:`kivy.clock`.
    `log_dir`: string
        Path of log directory.
    `log_enable`: int, 0 or 1
        Activate file logging. 0 is disabled, 1 is enabled.

        .. note::
            Logging output can also be controlled by the environment variables
            ``KIVY_LOG_MODE``, ``KIVY_NO_FILELOG`` and ``KIVY_NO_CONSOLELOG``.
            More information is provided in the :mod:`kivy.logger` module.

    `log_level`: string, one of |log_levels|
        Set the minimum log level to use.
    `log_name`: string
        Format string to use for the filename of log file.

    `log_maxfiles`: int
        Keep log_maxfiles recent logfiles while purging the log directory. Set
        'log_maxfiles' to -1 to disable logfile purging (eg keep all logfiles).

        .. note::
            You end up with 'log_maxfiles + 1' logfiles because the logger
            adds a new one after purging.

    `window_icon`: string
        Path of the window icon. Use this if you want to replace the default
        pygame icon.

:postproc:

    `double_tap_distance`: float
        Maximum distance allowed for a double tap, normalized inside the range
        0 - 1000.
    `double_tap_time`: int
        Time allowed for the detection of double tap, in milliseconds.
    `ignore`: list of tuples
        List of regions where new touches are ignored.
        This configuration token can be used to resolve hotspot problems
        with DIY hardware. The format of the list must be::

            ignore = [(xmin, ymin, xmax, ymax), ...]

        All the values must be inside the range 0 - 1.
    `jitter_distance`: int
        Maximum distance for jitter detection, normalized inside the range 0
        - 1000.
    `jitter_ignore_devices`: string, separated with commas
        List of devices to ignore from jitter detection.
    `retain_distance`: int
        If the touch moves more than is indicated by retain_distance, it will
        not be retained. Argument should be an int between 0 and 1000.
    `retain_time`: int
        Time allowed for a retain touch, in milliseconds.
    `triple_tap_distance`: float
        Maximum distance allowed for a triple tap, normalized inside the range
        0 - 1000.
    `triple_tap_time`: int
        Time allowed for the detection of triple tap, in milliseconds.

:graphics:
    `borderless`: int, one of 0 or 1
        If set to `1`, removes the window border/decoration. Window resizing
        must also be disabled to hide the resizing border.
    `custom_titlebar`: int, one of 0 or 1
        If set to `1`, removes the window border and allows user to set a Widget
        as a titlebar
        see :meth:`~kivy.core.window.WindowBase.set_custom_titlebar`
        for detailed usage
    `custom_titlebar_border`: int, defaults to 5
        sets the how many pixles off the border should be used as the
        rezising frame
    `window_state`: string , one of 'visible', 'hidden', 'maximized'
                    or 'minimized'

        Sets the window state, defaults to 'visible'. This option is available
        only for the SDL2 window provider and it should be used on desktop
        OSes.
    `fbo`: string, one of 'hardware', 'software' or 'force-hardware'
        Selects the FBO backend to use.
    `fullscreen`: int or string, one of 0, 1, 'fake' or 'auto'
        Activate fullscreen. If set to `1`, a resolution of `width`
        times `height` pixels will be used.
        If set to `auto`, your current display's resolution will be
        used instead. This is most likely what you want.
        If you want to place the window in another display,
        use `fake`, or set the `borderless` option from the graphics section,
        then adjust `width`, `height`, `top` and `left`.
    `height`: int
        Height of the :class:`~kivy.core.window.Window`, not used if
        `fullscreen` is set to `auto`.
    `left`: int
        Left position of the :class:`~kivy.core.window.Window`.
    `maxfps`: int, defaults to 60
        Maximum FPS allowed.

        .. warning::
            Setting maxfps to 0 will lead to max CPU usage.

    'multisamples': int, defaults to 2
        Sets the `MultiSample Anti-Aliasing (MSAA)
        <http://en.wikipedia.org/wiki/Multisample_anti-aliasing>`_ level.
        Increasing this value results in smoother graphics but at the cost of
        processing time.

        .. note::
           This feature is limited by device hardware support and will have no
           effect on devices which do not support the level of MSAA requested.

    `position`: string, one of 'auto' or 'custom'
        Position of the window on your display. If `auto` is used, you have no
        control of the initial position: `top` and `left` are ignored.
    `show_cursor`: int, one of 0 or 1
        Set whether or not the cursor is shown on the window.
    `top`: int
        Top position of the :class:`~kivy.core.window.Window`.
    `resizable`: int, one of 0 or 1
        If 0, the window will have a fixed size. If 1, the window will be
        resizable.
    `rotation`: int, one of 0, 90, 180 or 270
        Rotation of the :class:`~kivy.core.window.Window`.
    `width`: int
        Width of the :class:`~kivy.core.window.Window`, not used if
        `fullscreen` is set to `auto`.
    `minimum_width`: int
        Minimum width to restrict the window to. (sdl2 only)
    `minimum_height`: int
        Minimum height to restrict the window to. (sdl2 only)
    `min_state_time`: float, defaults to .035
        Minimum time for widgets to display a given visual state.
        This attrib is currently used by widgets like
        :class:`~kivy.uix.dropdown.DropDown` &
        :class:`~kivy.uix.behaviors.buttonbehavior.ButtonBehavior` to
        make sure they display their current visual state for the given
        time.
    `always_on_top`: int, one of ``0`` or ``1``, defaults to ``0``
        When enabled, the window will be brought to the front and will keep
        the window above the rest. Only works for the sdl2 window provider.
        ``0`` is disabled, ``1`` is enabled.
    `show_taskbar_icon`: int, one of ``0`` or ``1``, defaults to ``1``
        Determines whether the app's icon will be added to the taskbar. Only
        applicable for the SDL2 window provider.
        ``0`` means the icon will not be shown in the taskbar and ``1`` means
        it will.
    `allow_screensaver`: int, one of 0 or 1, defaults to 1
        Allow the device to show a screen saver, or to go to sleep
        on mobile devices. Only works for the sdl2 window provider.
    `vsync`: `none`, empty value, or integers
        Whether vsync is enabled, currently only used with sdl2 window.
        Possible values are `none` or empty value -- leaves it unchanged,
        ``0`` -- disables vsync, ``1`` or larger -- sets vsync interval,
        ``-1`` sets adaptive vsync. It falls back to 1 if setting to ``2+``
        or ``-1`` failed. See ``SDL_GL_SetSwapInterval``.
    `verify_gl_main_thread`: int, 1 or 0, defaults to 1
        Whether to check if code that changes any gl instructions is
        running outside the main thread and then raise an error.

:input:

    You can create new input devices using this syntax::

        # example of input provider instance
        yourid = providerid,parameters

        # example for tuio provider
        default = tuio,127.0.0.1:3333
        mytable = tuio,192.168.0.1:3334

    .. seealso::

        Check the providers in :mod:`kivy.input.providers` for the syntax to
        use inside the configuration file.

:widgets:

    `scroll_distance`: int
        Default value of the
        :attr:`~kivy.uix.scrollview.ScrollView.scroll_distance`
        property used by the :class:`~kivy.uix.scrollview.ScrollView` widget.
        Check the widget documentation for more information.

    `scroll_friction`: float
        Default value of the
        :attr:`~kivy.uix.scrollview.ScrollView.scroll_friction`
        property used by the :class:`~kivy.uix.scrollview.ScrollView` widget.
        Check the widget documentation for more information.

        .. deprecated:: 1.7.0
            Please use
            :class:`~kivy.uix.scrollview.ScrollView.effect_cls` instead.

    `scroll_timeout`: int
        Default value of the
        :attr:`~kivy.uix.scrollview.ScrollView.scroll_timeout`
        property used by the  :class:`~kivy.uix.scrollview.ScrollView` widget.
        Check the widget documentation for more information.

    `scroll_stoptime`: int
        Default value of the
        :attr:`~kivy.uix.scrollview.ScrollView.scroll_stoptime`
        property used by the :class:`~kivy.uix.scrollview.ScrollView` widget.
        Check the widget documentation for more information.

        .. deprecated:: 1.7.0
            Please use
            :class:`~kivy.uix.scrollview.ScrollView.effect_cls` instead.

    `scroll_moves`: int
        Default value of the
        :attr:`~kivy.uix.scrollview.ScrollView.scroll_moves`
        property used by the :class:`~kivy.uix.scrollview.ScrollView` widget.
        Check the widget documentation for more information.

        .. deprecated:: 1.7.0
            Please use
            :class:`~kivy.uix.scrollview.ScrollView.effect_cls` instead.

:modules:

    You can activate modules with this syntax::

        modulename =

    Anything after the = will be passed to the module as arguments.
    Check the specific module's documentation for a list of accepted
    arguments.

.. versionadded:: 2.2.0
    `always_on_top` have been added to the `graphics` section.
    `show_taskbar_icon` have been added to the `graphics` section.

.. versionchanged:: 2.2.0
    `implementation` has been added to the network section.

.. versionchanged:: 2.1.0
    `vsync` has been added to the graphics section.
    `verify_gl_main_thread` has been added to the graphics section.

.. versionchanged:: 1.10.0
    `min_state_time`  and `allow_screensaver` have been added
    to the `graphics` section.
    `kivy_clock` has been added to the kivy section.
    `default_font` has beed added to the kivy section.
    `useragent` has been added to the network section.

.. versionchanged:: 1.9.0
    `borderless` and `window_state` have been added to the graphics section.
    The `fake` setting of the `fullscreen` option has been deprecated,
    use the `borderless` option instead.
    `pause_on_minimize` has been added to the kivy section.

.. versionchanged:: 1.8.0
    `systemanddock` and `systemandmulti` has been added as possible values for
    `keyboard_mode` in the kivy section. `exit_on_escape` has been added
    to the kivy section.

.. versionchanged:: 1.2.0
    `resizable` has been added to graphics section.

.. versionchanged:: 1.1.0
    tuio no longer listens by default. Window icons are not copied to
    user directory anymore. You can still set a new window icon by using the
    ``window_icon`` config setting.

.. versionchanged:: 1.0.8
    `scroll_timeout`, `scroll_distance` and `scroll_friction` have been added.
    `list_friction`, `list_trigger_distance` and `list_friction_bound`
    have been removed. `keyboard_type` and `keyboard_layout` have been
    removed from the widget. `keyboard_mode` and `keyboard_layout` have
    been added to the kivy section.
'''
__all__ = ('Config', 'ConfigParser')
_is_rpi = ...
KIVY_CONFIG_VERSION = ...
Config = ...
class ConfigParser(PythonConfigParser):
    '''Enhanced ConfigParser class that supports the addition of default
    sections and default values.

    By default, the kivy ConfigParser instance, :attr:`~kivy.config.Config`,
    is named `'kivy'` and the ConfigParser instance used by the
    :meth:`App.build_settings <~kivy.app.App.build_settings>` method is named
    `'app'`.

    :Parameters:
        `name`: string
            The name of the instance. See :attr:`name`. Defaults to `''`.

    .. versionchanged:: 1.9.0
        Each ConfigParser can now be :attr:`named <name>`. You can get the
        ConfigParser associated with a name using :meth:`get_configparser`.
        In addition, you can now control the config values with
        :class:`~kivy.properties.ConfigParserProperty`.

    .. versionadded:: 1.0.7
    '''
    def __init__(self, name=..., **kwargs) -> None:
        ...
    
    def add_callback(self, callback, section=..., key=...): # -> None:
        '''Add a callback to be called when a specific section or key has
        changed. If you don't specify a section or key, it will call the
        callback for all section/key changes.

        Callbacks will receive 3 arguments: the section, key and value.

        .. versionadded:: 1.4.1
        '''
        ...
    
    def remove_callback(self, callback, section=..., key=...): # -> None:
        '''Removes a callback added with :meth:`add_callback`.
        :meth:`remove_callback` must be called with the same parameters as
        :meth:`add_callback`.

        Raises a `ValueError` if not found.

        .. versionadded:: 1.9.0
        '''
        ...
    
    def read(self, filename): # -> None:
        '''Read only one filename. In contrast to the original ConfigParser of
        Python, this one is able to read only one file at a time. The last
        read file will be used for the :meth:`write` method.

        .. versionchanged:: 1.9.0
            :meth:`read` now calls the callbacks if read changed any values.

        '''
        ...
    
    def set(self, section, option, value):
        '''Functions similarly to PythonConfigParser's set method, except that
        the value is implicitly converted to a string.
        '''
        ...
    
    def setall(self, section, keyvalues): # -> None:
        '''Sets multiple key-value pairs in a section. keyvalues should be a
        dictionary containing the key-value pairs to be set.
        '''
        ...
    
    def get(self, section, option, **kwargs):
        ...
    
    def setdefaults(self, section, keyvalues): # -> None:
        '''Set multiple key-value defaults in a section. keyvalues should be
        a dictionary containing the new key-value defaults.
        '''
        ...
    
    def setdefault(self, section, option, value): # -> None:
        '''Set the default value for an option in the specified section.
        '''
        ...
    
    def getdefault(self, section, option, defaultvalue):
        '''Get the value of an option in the specified section. If not found,
        it will return the default value.
        '''
        ...
    
    def getdefaultint(self, section, option, defaultvalue): # -> int:
        '''Get the value of an option in the specified section. If not found,
        it will return the default value. The value will always be
        returned as an integer.

        .. versionadded:: 1.6.0
        '''
        ...
    
    def adddefaultsection(self, section): # -> None:
        '''Add a section if the section is missing.
        '''
        ...
    
    def write(self): # -> bool:
        '''Write the configuration to the last file opened using the
        :meth:`read` method.

        Return True if the write finished successfully, False otherwise.
        '''
        ...
    
    def update_config(self, filename, overwrite=...): # -> None:
        '''Upgrade the configuration based on a new default config file.
        Overwrite any existing values if overwrite is True.
        '''
        ...
    
    @staticmethod
    def get_configparser(name): # -> None:
        '''Returns the :class:`ConfigParser` instance whose name is `name`, or
        None if not found.

        :Parameters:
            `name`: string
                The name of the :class:`ConfigParser` instance to return.
        '''
        ...
    
    _named_configs = ...
    _name = ...
    @property
    def name(self): # -> str:
        ''' The name associated with this ConfigParser instance, if not `''`.
        Defaults to `''`. It can be safely changed dynamically or set to `''`.

        When a ConfigParser is given a name, that config object can be
        retrieved using :meth:`get_configparser`. In addition, that config
        instance can also be used with a
        :class:`~kivy.properties.ConfigParserProperty` instance that set its
        `config` value to this name.

        Setting more than one ConfigParser with the same name will raise a
        `ValueError`.
        '''
        ...
    
    @name.setter
    def name(self, value): # -> None:
        ...
    


if notenviron.get('KIVY_DOC_INCLUDE'):
    Config = ...
    version = ...
    need_save = ...
