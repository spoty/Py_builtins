callable(object)

    Return True if the object argument appears callable, False if not. If this
    returns true, it is still possible that a call fails, but if it is false,
    calling object will never succeed. Note that classes are callable (calling a
    class returns a new instance); class instances are callable if they have a
    __call__() method.
