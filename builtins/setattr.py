
setattr(object, name, value)

    This is the counterpart of getattr(). The arguments are an object, a string
    and an arbitrary value. The string may name an existing attribute or a new
    attribute. The function assigns the value to the attribute, provided the
    object allows it. For example, setattr(x, 'foobar', 123) is equivalent to
    x.foobar = 123.
