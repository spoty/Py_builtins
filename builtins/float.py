 float([x])

    Convert a string or a number to floating point. If the argument is a string,
    it must contain a possibly signed decimal or floating point number, possibly
    embedded in whitespace. The argument may also be [+|-]nan or [+|-]inf.
    Otherwise, the argument may be a plain or long integer or a floating point
    number, and a floating point number with the same value (within Python’s
    floating point precision) is returned. If no argument is given, returns 0.0.

    Note

    When passing in a string, values for NaN and Infinity may be returned,
    depending on the underlying C library. Float accepts the strings nan, inf
    and -inf for NaN and positive or negative infinity. The case and a leading +
    are ignored as well as a leading - is ignored for NaN. Float always
    represents NaN and infinity as nan, inf or -inf.
