"""
This type stub file was generated by pyright.
"""

from os import environ
from typing import Any

from kivy.lang.parser import ParserException

"""
Builder
======

Class used for the registering and application of rules for specific widgets.
"""
__all__ = ("Observable", "Builder", "BuilderBase", "BuilderException")
trace = ...
Instruction = ...
_delayed_start = ...

class BuilderException(ParserException):
    """Exception raised when the Builder fails to apply a rule on a widget."""

    ...

def get_proxy(widget): ...
def custom_callback(__kvlang__, idmap, *largs, **kwargs): ...
def call_fn(args, instance, v): ...
def delayed_call_fn(args, instance, v): ...
def update_intermediates(base, keys, bound, s, fn, args, instance, value):  # -> None:
    """Function that is called when an intermediate property is updated
    and `rebind` of that property is True. In that case, we unbind
    all bound funcs that were bound to attrs of the old value of the
    property and rebind them to the new value of the property.

    For example, if the rule is `self.a.b.c.d`, then when b is changed, we
    unbind from `b`, `c` and `d`, if they were bound before (they were not
    None and `rebind` of the respective properties was True) and we rebind
    to the new values of the attrs `b`, `c``, `d` that are not None and
    `rebind` is True.

    :Parameters:
        `base`
            A (proxied) ref to the base widget, `self` in the example
            above.
        `keys`
            A list of the name off the attrs of `base` being watched. In
            the example above it'd be `['a', 'b', 'c', 'd']`.
        `bound`
            A list 4-tuples, each tuple being (widget, attr, callback, uid)
            representing callback functions bound to the attributed `attr`
            of `widget`. `uid` is returned by `fbind` when binding.
            The callback may be None, in which case the attr
            was not bound, but is there to be able to walk the attr tree.
            E.g. in the example above, if `b` was not an eventdispatcher,
            `(_b_ref_, `c`, None)` would be added to the list so we can get
            to `c` and `d`, which may be eventdispatchers and their attrs.
        `s`
            The index in `keys` of the of the attr that needs to be
            updated. That is all the keys from `s` and further will be
            rebound, since the `s` key was changed. In bound, the
            corresponding index is `s - 1`. If `s` is None, we start from
            1 (first attr).
        `fn`
            The function to be called args, `args` on bound callback.
    """
    ...

def create_handler(iself, element, key, value, rule, idmap, delayed=...): ...

class BuilderBase:
    """The Builder is responsible for creating a :class:`Parser` for parsing a
    kv file, merging the results into its internal rules, templates, etc.

    By default, :class:`Builder` is a global Kivy instance used in widgets
    that you can use to load other kv files in addition to the default ones.
    """

    def __init__(self) -> None: ...
    @classmethod
    def create_from(cls, builder):  # -> Self@BuilderBase:
        """Creates a instance of the class, and initializes to the state of
        ``builder``.

        :param builder: The builder to initialize from.
        :return: A new instance of this class.
        """
        ...
    def load_file(
        self, filename: str, encoding: str = ..., **kwargs: Any
    ) -> Any | None:
        """Insert a file into the language builder and return the root widget
        (if defined) of the kv file.

        :parameters:
            `rulesonly`: bool, defaults to False
                If True, the Builder will raise an exception if you have a root
                widget inside the definition.

            `encoding`: File character encoding. Defaults to utf-8,
        """
        ...
    def unload_file(self, filename):  # -> None:
        """Unload all rules associated with a previously imported file.

        .. versionadded:: 1.0.8

        .. warning::

            This will not remove rules or templates already applied/used on
            current widgets. It will only effect the next widgets creation or
            template invocation.
        """
        ...
    def load_string(self, string, **kwargs):  # -> Any | _ | None:
        '''Insert a string into the Language Builder and return the root widget
        (if defined) of the kv string.

        :Parameters:
            `rulesonly`: bool, defaults to False
                If True, the Builder will raise an exception if you have a root
                widget inside the definition.
            `filename`: str, defaults to None
                If specified, the filename used to index the kv rules.

        The filename parameter can be used to unload kv strings in the same way
        as you unload kv files. This can be achieved using pseudo file names
        e.g.::

            Build.load_string("""
                <MyRule>:
                    Label:
                        text="Hello"
            """, filename="myrule.kv")

        can be unloaded via::

            Build.unload_file("myrule.kv")

        '''
        ...
    def template(self, *args, **ctx):  # -> Any:
        """Create a specialized template using a specific context.

        .. versionadded:: 1.0.5

        With templates, you can construct custom widgets from a kv lang
        definition by giving them a context. Check :ref:`Template usage
        <template_usage>`.
        """
        ...
    def apply_rules(
        self,
        widget,
        rule_name,
        ignored_consts=...,
        rule_children=...,
        dispatch_kv_post=...,
    ):  # -> None:
        """Search all the rules that match the name `rule_name`
        and apply them to `widget`.

        .. versionadded:: 1.10.0

        :Parameters:

            `widget`: :class:`~kivy.uix.widget.Widget`
                The widget to whom the matching rules should be applied to.
            `ignored_consts`: set
                A set or list type whose elements are property names for which
                constant KV rules (i.e. those that don't create bindings) of
                that widget will not be applied. This allows e.g. skipping
                constant rules that overwrite a value initialized in python.
            `rule_children`: list
                If not ``None``, it should be a list that will be populated
                with all the widgets created by the kv rules being applied.

                .. versionchanged:: 1.11.0

            `dispatch_kv_post`: bool
                Normally the class `Widget` dispatches the `on_kv_post` event
                to widgets created during kv rule application.
                But if the rules are manually applied by calling :meth:`apply`,
                that may not happen, so if this is `True`, we will dispatch the
                `on_kv_post` event where needed after applying the rules to
                `widget` (we won't dispatch it for `widget` itself).

                Defaults to False.

                .. versionchanged:: 1.11.0
        """
        ...
    def apply(
        self, widget, ignored_consts=..., rule_children=..., dispatch_kv_post=...
    ):  # -> None:
        """Search all the rules that match the widget and apply them.

        :Parameters:

            `widget`: :class:`~kivy.uix.widget.Widget`
                The widget whose class rules should be applied to this widget.
            `ignored_consts`: set
                A set or list type whose elements are property names for which
                constant KV rules (i.e. those that don't create bindings) of
                that widget will not be applied. This allows e.g. skipping
                constant rules that overwrite a value initialized in python.
            `rule_children`: list
                If not ``None``, it should be a list that will be populated
                with all the widgets created by the kv rules being applied.

                .. versionchanged:: 1.11.0

            `dispatch_kv_post`: bool
                Normally the class `Widget` dispatches the `on_kv_post` event
                to widgets created during kv rule application.
                But if the rules are manually applied by calling :meth:`apply`,
                that may not happen, so if this is `True`, we will dispatch the
                `on_kv_post` event where needed after applying the rules to
                `widget` (we won't dispatch it for `widget` itself).

                Defaults to False.

                .. versionchanged:: 1.11.0
        """
        ...
    def match(self, widget):  # -> list[Unknown]:
        """Return a list of :class:`ParserRule` objects matching the widget."""
        ...
    def match_rule_name(self, rule_name):  # -> list[Unknown]:
        """Return a list of :class:`ParserRule` objects matching the widget."""
        ...
    def sync(self):  # -> None:
        """Execute all the waiting operations, such as the execution of all the
        expressions related to the canvas.

        .. versionadded:: 1.7.0
        """
        ...
    def unbind_widget(self, uid):  # -> None:
        """Unbind all the handlers created by the KV rules of the
        widget. The :attr:`kivy.uix.widget.Widget.uid` is passed here
        instead of the widget itself, because Builder is using it in the
        widget destructor.

        This effectively clears all the KV rules associated with this widget.
        For example:

        .. code-block:: python

            >>> w = Builder.load_string('''
            ... Widget:
            ...     height: self.width / 2. if self.disabled else self.width
            ...     x: self.y + 50
            ... ''')
            >>> w.size
            [100, 100]
            >>> w.pos
            [50, 0]
            >>> w.width = 500
            >>> w.size
            [500, 500]
            >>> Builder.unbind_widget(w.uid)
            >>> w.width = 222
            >>> w.y = 500
            >>> w.size
            [222, 500]
            >>> w.pos
            [50, 500]

        .. versionadded:: 1.7.2
        """
        ...
    def unbind_property(self, widget, name):  # -> None:
        """Unbind the handlers created by all the rules of the widget that set
        the name.

        This effectively clears all the rules of widget that take the form::

            name: rule

        For example:

        .. code-block:: python

            >>> w = Builder.load_string('''
            ... Widget:
            ...     height: self.width / 2. if self.disabled else self.width
            ...     x: self.y + 50
            ... ''')
            >>> w.size
            [100, 100]
            >>> w.pos
            [50, 0]
            >>> w.width = 500
            >>> w.size
            [500, 500]
            >>> Builder.unbind_property(w, 'height')
            >>> w.width = 222
            >>> w.size
            [222, 500]
            >>> w.y = 500
            >>> w.pos
            [550, 500]

        .. versionadded:: 1.9.1
        """
        ...

Builder: BuilderBase = ...
if "KIVY_PROFILE_LANG" in environ:
    def match_rule(fn, index, rule): ...
    def dump_builder_stats(): ...