"""
    basestring()

    This abstract type is the superclass for str and unicode. It cannot be
    called or instantiated, but it can be used to test whether an object is an
    instance of str or unicode.

    isinstance(obj, basestring)

    is equivalent to

    isinstance(obj, (str, unicode)).
"""


# This stuff is completely different in Python3

# types not longer has StringType str is always unicode basestring no longer
# exists

# So try not to sprinkle that stuff through your code too much if you might ever
# need to port it

print isinstance("ahoj", str)
# True

print isinstance("ahoj", (str, unicode))
# True

print isinstance(u'ahoj', str)
# False

print isinstance(u'ahoj', basestring)
# True


