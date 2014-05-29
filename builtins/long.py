 long(x,base=10)

    Convert a string or number to a long integer. If the argument is a string,
    it must contain a possibly signed number of arbitrary size, possibly
    embedded in whitespace. The base argument is interpreted in the same way as
    for int(), and may only be given when x is a string. Otherwise, the argument
    may be a plain or long integer or a floating point number, and a long
    integer with the same value is returned. Conversion of floating point
    numbers to integers truncates (towards zero). If no arguments are given,
    returns 0L.

    The long type is described in Numeric Types — int, float, long, complex.
