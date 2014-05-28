 unicode(object[,encoding[,errors]])

    Return the Unicode string version of object using one of the following
    modes:

    If encoding and/or errors are given, unicode() will decode the object which
    can either be an 8-bit string or a character buffer using the codec for
    encoding. The encoding parameter is a string giving the name of an encoding;
    if the encoding is not known, LookupError is raised. Error handling is done
    according to errors; this specifies the treatment of characters which are
    invalid in the input encoding. If errors is 'strict' (the default), a
    ValueError is raised on errors, while a value of 'ignore' causes errors to
    be silently ignored, and a value of 'replace' causes the official Unicode
    replacement character, U+FFFD, to be used to replace input characters which
    cannot be decoded. See also the codecs module.

    If no optional parameters are given, unicode() will mimic the behaviour of
    str() except that it returns Unicode strings instead of 8-bit strings. More
    precisely, if object is a Unicode string or subclass it will return that
    Unicode string without any additional decoding applied.

    For objects which provide a __unicode__() method, it will call this method
    without arguments to create a Unicode string. For all other objects, the
    8-bit string version or representation is requested and then converted to a
    Unicode string using the codec for the default encoding in 'strict' mode.

    For more information on Unicode strings see Sequence Types — str, unicode,
    list, tuple, bytearray, buffer, xrange which describes sequence
    functionality (Unicode strings are sequences), and also the string-specific
    methods described in the String Methods section. To output formatted strings
    use template strings or the % operator described in the String Formatting
    Operations section. In addition see the String Services section. See also
    str().

    http://lucumr.pocoo.org/2014/1/5/unicode-in-2-and-3/
