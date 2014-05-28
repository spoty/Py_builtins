 format(value[,format_spec])

    Convert a value to a “formatted” representation, as controlled by
    format_spec. The interpretation of format_spec will depend on the type of
    the value argument, however there is a standard formatting syntax that is
    used by most built-in types: Format Specification Mini-Language.

    Note

    format(value, format_spec) merely calls value.__format__(format_spec).

    more about formating:
    https://docs.python.org/2/library/string.html#formatspec
