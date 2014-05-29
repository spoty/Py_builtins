
round(number[, ndigits])

    Return the floating point value number rounded to ndigits digits after the
    decimal point. If ndigits is omitted, it defaults to zero. The result is a
    floating point number. Values are rounded to the closest multiple of 10 to
    the power minus ndigits; if two multiples are equally close, rounding is
    done away from 0 (so. for example, round(0.5) is 1.0 and round(-0.5) is
    -1.0).

    Note

    The behavior of round() for floats can be surprising: for example,
    round(2.675, 2) gives 2.67 instead of the expected 2.68. This is not a bug:
    it’s a result of the fact that most decimal fractions can’t be represented
    exactly as a float. See Floating Point Arithmetic: Issues and Limitations
    for more information.
