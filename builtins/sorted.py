
 sorted(iterable[,cmp[,key[,reverse]]])

    Return a new sorted list from the items in iterable.

    The optional arguments cmp, key, and reverse have the same meaning as those
    for the list.sort() method (described in section Mutable Sequence Types).

    cmp specifies a custom comparison function of two arguments (iterable
    elements) which should return a negative, zero or positive number depending
    on whether the first argument is considered smaller than, equal to, or
    larger than the second argument: cmp=lambda x,y: cmp(x.lower(), y.lower()).
    The default value is None.

    key specifies a function of one argument that is used to extract a
    comparison key from each list element: key=str.lower. The default value is
    None (compare the elements directly).

    reverse is a boolean value. If set to True, then the list elements are
    sorted as if each comparison were reversed.

    In general, the key and reverse conversion processes are much faster than
    specifying an equivalent cmp function. This is because cmp is called
    multiple times for each list element while key and reverse touch each
    element only once. Use functools.cmp_to_key() to convert an old-style cmp
    function to a key function.

    For sorting examples and a brief sorting tutorial, see Sorting HowTo.

    https://wiki.python.org/moin/HowTo/Sorting/
