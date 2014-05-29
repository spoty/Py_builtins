 xrange(start,stop[,step])

    This function is very similar to range(), but returns an xrange object
    instead of a list. This is an opaque sequence type which yields the same
    values as the corresponding list, without actually storing them all
    simultaneously. The advantage of xrange() over range() is minimal (since
    xrange() still has to create the values when asked for them) except when a
    very large range is used on a memory-starved machine or when all of the
    range’s elements are never used (such as when the loop is usually terminated
    with break).



range creates a list, so if you do range(1, 10000000) it creates a list in
memory with 10000000 elements.

xrange is a generator, so it is a sequence object is a that evaluates lazily.



One difference is that from versions of Python 3.0 and later,  xrange
doesn't exist, and range takes over the behavior of what was formerly
xrange.

So presumably you're asking about Python 2.x


In Python 2.x, range() generates a list, possibly a very large one.
Sometimes that's exactly what you need.  But other times, you're just
using the list as an iterable, perhaps as a counter, or simply as a way
to make a loop go a fixed number of times.

xrange(), usually more efficient for speed, and certainly for space,
generates an iterable.  So it's interchangeable in a for loop, for example.

In general, if you're going to discard the list immediately after using
it, you should be using the iterable form, not the list form.


In Python 3.x, if you really need a list, you can trivially convert an
iterable into a list with the list "function."

mylist = list(range(4))
