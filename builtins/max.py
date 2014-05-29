 max(arg1,arg2,*args[,key])

    Return the largest item in an iterable or the largest of two or more
    arguments.

    If one positional argument is provided, iterable must be a non-empty
    iterable (such as a non-empty string, tuple or list). The largest item in
    the iterable is returned. If two or more positional arguments are provided,
    the largest of the positional arguments is returned.

    The optional key argument specifies a one-argument ordering function like
    that used for list.sort(). The key argument, if supplied, must be in keyword
    form (for example, max(a,b,c,key=func)).

max(range(10)) # 9
