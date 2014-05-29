
reload(module)

    Reload a previously imported module. The argument must be a module object,
    so it must have been successfully imported before. This is useful if you
    have edited the module source file using an external editor and want to try
    out the new version without leaving the Python interpreter. The return value
    is the module object (the same as the module argument).

 Examples:
    I have a long-running Python server and would like to be able to upgrade
    a service without restarting the server. What's the best way do do this?
A:
You can reload a module when it has already been imported by using the reload
builtin function:

import foo

while True:
# Do some things.
    if is_changed(foo):
        foo =
reload(foo)

I think that this is what you want. Web servers like Django's development server
use this so that you can see the effects of your code changes without restarting
the server process itself.

To quote from the docs:

    Python modules’ code is recompiled and the module-level code reexecuted,
    defining a new set of objects which are bound to names in the module’s
    dictionary. The init function of extension modules is not called a second
    time. As with all other objects in Python the old objects are only reclaimed
    after their reference counts drop to zero. The names in the module namespace
    are updated to point to any new or changed objects. Other references to the
    old objects (such as names external to the module) are not rebound to refer
    to the new objects and must be updated in each namespace where they occur if
    that is desired.

As you noted in your question, you'll have to reconstruct Foo objects if the Foo
class resides in the foo module.
