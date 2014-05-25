""" print(*objects,sep='',end='\n',file=sys.stdout)

    Print objects to the stream file, separated by sep and followed by end. sep,
    end and file, if present, must be given as keyword arguments.

    All non-keyword arguments are converted to strings like str() does and
    written to the stream, separated by sep and followed by end. Both sep and
    end must be strings; they can also be None, which means to use the default
    values. If no objects are given, print() will just write end.

    The file argument must be an object with a write(string) method; if it is
    not present or None, sys.stdout will be used. Output buffering is determined
    by file. Use file.flush() to ensure, for instance, immediate appearance on a
    screen.

    Note

    This function is not normally available as a built-in since the name print
    is recognized as the print statement. To disable the statement and use the
    print() function, use this future statement at the top of your module:

    from __future__ import print_function"""

