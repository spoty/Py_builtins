 unichr(i)

    Return the Unicode string of one character whose Unicode code is the integer
    i. For example, unichr(97) returns the string u'a'. This is the inverse of
    ord() for Unicode strings. The valid range for the argument depends how
    Python was configured – it may be either UCS2 [0..0xFFFF] or UCS4
    [0..0x10FFFF]. ValueError is raised otherwise. For ASCII and 8-bit strings
    see chr().
