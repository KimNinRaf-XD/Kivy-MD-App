"""
This type stub file was generated by pyright.
"""

import logging

"""
Kivy Logging
============

By default, Kivy provides a logging system based on the standard Python
`logging <https://docs.python.org/3/library/logging.html>`_ module with
several additional features designed to be more convenient. These features
include:

 * simplied usage (single instance, simple configuration, works by default)
 * color-coded output on supported terminals
 * output to ``stderr`` by default
 * message categorization via colon separation
 * access to log history even if logging is disabled
 * built-in handling of various cross-platform considerations
 * any stray output written to ``sys.stderr`` is captured, and stored in the log
   file as a warning.

These features are configurable via the Config file or environment variables -
including falling back to only using the standard Python system.

Logger object
=============

The Kivy ``Logger`` class provides a singleton logging.logger instance.

As well as the standard logging levels (``debug``, ``info``,
``warning``, ``error`` and ``critical``), an additional ``trace`` level is
available.

Example Usage
-------------

Use the ``Logger`` as you would a standard Python logger. ::

    from kivy.logger import Logger

    Logger.info('title: This is a info message.')
    Logger.debug('title: This is a debug message.')

    try:
        raise Exception('bleh')
    except Exception:
        Logger.exception('Something happened!')

The message passed to the logger is split into two parts separated by a colon
(:). The first part is used as a title and the second part is used as the
message. This way, you can "categorize" your messages easily. ::

    Logger.info('Application: This is a test')

    # will appear as

    [INFO   ] [Application ] This is a test

You can change the logging level at any time using the ``setLevel`` method. ::

    from kivy.logger import Logger, LOG_LEVELS

    Logger.setLevel(LOG_LEVELS["debug"])

.. versionchanged:: 2.2.0

Interaction with other logging
------------------------------

The Kivy logging system will, by default, present all log messages sent from
any logger - e.g. from third-party libraries.

Additional handlers may be added.

.. warning:: Handlers that output to ``sys.stderr`` may cause loops, as stderr
   output is reported as a warning log message.

Logger Configuration
====================

Kivy Log Mode
-------------

At the highest level, Kivy's logging system is controlled by an environment
variable ``KIVY_LOG_MODE``. It may be given any of three values:
``KIVY``, ``PYTHON``, ``MIXED``

.. versionadded: 2.2.0

KIVY Mode (default)
^^^^^^^^^^^^^^^^^^^

In ``KIVY`` mode, all Kivy handlers are attached to the root logger, so all log
messages in the system are output to the Kivy log files and to the console. Any
stray output to ``sys.stderr`` is logged as a warning.

If you are writing an entire Kivy app from scratch, this is the most convenient
mode.

PYTHON Mode
^^^^^^^^^^^

In ``PYTHON`` mode, no handlers are added, and ``sys.stderr`` output is not
captured. It is left to the client to add appropriate handlers. (If none are
added, the ``logging`` module will output them to ``stderr``.)

Messages logged with ``Logger`` will be propagated to the root logger, from a
logger named ``kivy``.

If the Kivy app is part of a much larger project which has its own logging
regimen, this is the mode that gives most control.

The ``kivy.logger`` file contains a number of ``logging.handler``,
``logging.formatter``, and other helper classes to allow
users to adopt the features of Kivy logging that they like, including the
stderr redirection.

MIXED Mode
^^^^^^^^^^

In ``MIXED`` mode, handlers are added to the Kivy's ``Logger`` object directly,
and propagation is turned off. ``sys.stderr`` is not redirected.

Messages logged with Kivy's ``Logger`` will appear in the Kivy log file and
output to the Console.

However, messages logged with other Python loggers will not be handled by Kivy
handlers. The client will need to add their own.

If you like the features of Kivy ``Logger``, but are writing a Kivy app that
relies on third-party libraries that don't use colon-separation of categorise
or depend on the display of the logger name, this mode provides a compromise.

Again, the ``kivy.logger`` file contains re-usable logging features that can be
used to get the best of both systems.

Config Files
------------

In ``KIVY`` and ``MIXED`` modes, the logger handlers can be controlled via the
Kivy configuration file::

    [kivy]
    log_level = info
    log_enable = 1
    log_dir = logs
    log_name = kivy_%y-%m-%d_%_.txt
    log_maxfiles = 100

More information about the allowed values are described in the
:mod:`kivy.config` module.

In addition, the environment variables ``KIVY_NO_FILELOG`` and
``KIVY_NO_CONSOLELOG`` can be used to turn off the installation of the
corresponding handlers.


Logger History
--------------

Even if the logger is not enabled, you still have access to the last 100
LogRecords::

    from kivy.logger import LoggerHistory

    print(LoggerHistory.history)
"""
__all__ = ("add_kivy_handlers", "ColonSplittingLogRecord", "ColoredLogRecord", "COLORS", "ConsoleHandler", "file_log_handler", "FileHandler", "is_color_terminal", "KivyFormatter", "LOG_LEVELS", "Logger", "LoggerHistory", "ProcessingStream", "UncoloredLogRecord")
Logger = ...
LOG_LEVELS = ...
class FileHandler(logging.Handler):
    history = ...
    filename = ...
    fd = ...
    log_dir = ...
    encoding = ...
    def purge_logs(self): # -> None:
        """Purge logs which exceed the maximum amount of log files,
        starting with the oldest creation timestamp (or edit-timestamp on Linux)
        """
        ...
    
    def emit(self, message): # -> None:
        ...
    


class LoggerHistory(logging.Handler):
    history = ...
    def emit(self, message): # -> None:
        ...
    
    @classmethod
    def clear_history(cls): # -> None:
        ...
    
    def flush(self): # -> None:
        ...
    


class ConsoleHandler(logging.StreamHandler):
    """
        Emits records to a stream (by default, stderr).

        However, if the msg starts with "stderr:" it is not formatted, but
        written straight to the stream.

        .. versionadded:: 2.2.0
    """
    def filter(self, record): # -> bool:
        ...
    


class ProcessingStream:
    """
        Stream-like object that takes each completed line written to it,
        adds a given prefix, and applies the given function to it.

        .. versionadded:: 2.2.0
    """
    def __init__(self, channel, func) -> None:
        ...
    
    def write(self, s): # -> None:
        ...
    
    def flush(self): # -> None:
        ...
    
    def isatty(self): # -> Literal[False]:
        ...
    


def logger_config_update(section, key, value): # -> None:
    ...

class ColonSplittingLogRecord(logging.LogRecord):
    """Clones an existing logRecord, but reformats the message field
    if it contains a colon.

    .. versionadded:: 2.2.0
    """
    def __init__(self, logrecord) -> None:
        ...
    


class ColoredLogRecord(logging.LogRecord):
    """Clones an existing logRecord, but reformats the levelname to add
    color, and the message to add bolding (where indicated by $BOLD
    and $RESET in the message).

    .. versionadded:: 2.2.0"""
    BLACK = ...
    RED = ...
    GREEN = ...
    YELLOW = ...
    BLUE = ...
    MAGENTA = ...
    CYAN = ...
    WHITE = ...
    RESET_SEQ = ...
    COLOR_SEQ = ...
    BOLD_SEQ = ...
    LEVEL_COLORS = ...
    def __init__(self, logrecord) -> None:
        ...
    


COLORS = ...
class UncoloredLogRecord(logging.LogRecord):
    """Clones an existing logRecord, but reformats the message
    to remove $BOLD/$RESET markup.

    .. versionadded:: 2.2.0"""
    def __init__(self, logrecord) -> None:
        ...
    


class KivyFormatter(logging.Formatter):
    """Split out first field in message marked with a colon,
    and either apply terminal color codes to the record, or strip
    out color markup if colored logging is not available.

    .. versionadded:: 2.2.0"""
    def __init__(self, *args, use_color=..., **kwargs) -> None:
        ...
    
    def format(self, record): # -> str:
        ...
    


def is_color_terminal(): # -> bool | Literal['']:
    """ Detect whether the environment supports color codes in output.

    .. versionadded:: 2.2.0
    """
    ...

Logger = ...
file_log_handler = ...
def add_kivy_handlers(logger): # -> None:
    """ Add Kivy-specific handlers to a logger.

    .. versionadded:: 2.2.0
    """
    ...

KIVY_LOG_MODE = ...
if KIVY_LOG_MODE == "KIVY":
    ...
else:
    ...