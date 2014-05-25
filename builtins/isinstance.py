# isinstance(object, classinfo)
"""
Return true

if the object argument is an instance of the classinfo argument, or
of a (direct, indirect or virtual) subclass thereof.

Also return true if

classinfo is a type object (new-style class) and object is an object of that
type or of a (direct, indirect or virtual) subclass thereof.

If object is not a class instance or an object of the given type, the function
always returns false. If classinfo is neither a class object nor a type object,
it may be a tuple of class or type objects, or may recursively contain other
such tuples (other sequence types are not accepted). If classinfo is not a
class, type, or tuple of classes, types, and such tuples, a TypeError exception
is raised.

Differences between isinstance() and type() in python
http://stackoverflow.com/questions/1549801/differences-between-isinstance-and-type-in-python
"""

x = 25
print isinstance(x, str)
