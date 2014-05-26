""" tuple([iterable])

    Return a tuple whose items are the same and in the same order as iterable‘s
    items. iterable may be a sequence, a container that supports iteration, or
    an iterator object. If iterable is already a tuple, it is returned
    unchanged. For instance, tuple('abc') returns ('a', 'b', 'c') and tuple([1,
    2, 3]) returns (1, 2, 3). If no argument is given, returns a new empty
    tuple, ().

    tuple is an immutable sequence type, as documented in Sequence Types — str,
    unicode, list, tuple, bytearray, buffer, xrange. For other containers see
    the built in dict, list, and set classes, and the collections module.

Tuples are fixed size in nature whereas lists are dynamic. In other words, a
tuple is immutable whereas a list is mutable.

    You can't add elements to a tuple. Tuples have no append or extend method.
    You can't remove elements from a tuple. Tuples have no remove or pop method.
    You can find elements in a tuple, since this doesn’t change the tuple.  You
    can also use the in operator to check if an element exists in the tuple.

    Tuples are faster than lists. If you're defining a constant set of values
    and all you're ever going to do with it is iterate through it, use a tuple
    instead of a list.

    It makes your code safer if you “write-protect” data that does not need to
    be changed. Using a tuple instead of a list is like having an implied assert
    statement that this data is constant, and that special thought (and a
    specific function) is required to override that.

    Some tuples can be used as dictionary keys (specifically, tuples that
contain immutable values like strings, numbers, and other tuples). Lists can
never be used as dictionary keys, because lists are not immutable. """
