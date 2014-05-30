 hex(x)

    Convert an integer number (of any size) to a lowercase hexadecimal string
    prefixed with “0x”, for example: >>>

    >>> hex(255)
    '0xff'
    >>> hex(-42)
    '-0x2a'
    >>> hex(1L)
    '0x1L'

    If x is not a Python int or long object, it has to define an __index__()
    method that returns an integer.

    See also int() for converting a hexadecimal string to an integer using a
    base of 16.
