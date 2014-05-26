""" filter(function,iterable)¶

    Construct a list from those elements of iterable for which function returns
    true. iterable may be either a sequence, a container which supports
    iteration, or an iterator. If iterable is a string or a tuple, the result
    also has that type; otherwise it is always a list. If function is None, the
    identity function is assumed, that is, all elements of iterable that are
    false are removed.

    Note that filter(function, iterable) is equivalent to [item for item in
    iterable if function(item)] if function is not None and [item for item in
    iterable if item] if function is None.

    The docs for python 3 say it returns an iterator

    "Construct an iterator from those elements of iterable for which function returns true."

    In python 2 it returned a list: see here.

"""
