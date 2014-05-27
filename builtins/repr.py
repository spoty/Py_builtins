"""     repr(object)

The str() function is meant to return representations of values which are fairly
human-readable, while repr() is meant to generate representations which can be
read by the interpreter (or will force a SyntaxError if there is no equivalent
syntax)

    Return a string containing a printable representation of an object. This is
the same value yielded by conversions (reverse quotes). It is sometimes useful
to be able to access this operation as an ordinary function. For many types,
this function makes an attempt to return a string that would yield an object
with the same value when passed to eval(), otherwise the representation is a
string enclosed in angle brackets that contains the name of the type of the
object together with additional information often including the name and address
of the object. A class can control what this function returns for its instances
by defining a __repr__() method.

MORE: http://stackoverflow.com/questions/1436703/difference-between-str-and-
repr-in-python
========
This is usually a question asked in many Python interviews: What is the
difference between the __str__ and __repr__ methods of a Python object. The same
question was asked by one of my colleagues, which got me researching.

In short __repr__ goal is to be unambigous and __str__ is to be readable.

The official Python documentation says __repr__ is used to compute the
“official” string representation of an object and __str__ is used to compute the
“informal” string representation of an object. The print statement and str()
built-in function uses __str__ to display the string representation of the
object while the repr() built-in function uses __repr__ to display the object.
Using this definition let us take an example to understand what the two methods
actually do.

Lets create a datetime object:

>>> import datetime today = datetime.datetime.now()

When I use the built-in function str() to display today:

>>> str(today) '2012-03-14 09:21:58.130922'

You can see that the date was displayed as a string in a way that the user can
understand the date and time. Now lets see when I use the built-in function
repr():

>>> repr(today) 'datetime.datetime(2012, 3, 14, 9, 21, 58, 130922)'

You can see that this also returned a string but the string was the “official”
representation of a datetime object. What does official mean? Using the
“official” string representation I can reconstruct the object:

>>> eval('datetime.datetime(2012, 3, 14, 9, 21, 58, 130922)')
datetime.datetime(2012, 3, 14, 9, 21, 58, 130922)

The eval() built-in function accepts a string and converts it to a datetime
object.

Most functions while trying to get the string representation use the __str__
function, if missing uses __repr__. Thus in a general every class you code must
have a __repr__ and if you think it would be useful to have a string version of
the object, as in the case of datetime create a __str__ function. """
