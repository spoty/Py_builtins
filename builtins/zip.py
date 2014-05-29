 zip([iterable, ...])

    This function returns a list of tuples, where the i-th tuple contains the
    i-th element from each of the argument sequences or iterables. The returned
    list is truncated in length to the length of the shortest argument sequence.
    When there are multiple arguments which are all of the same length, zip() is
    similar to map() with an initial argument of None. With a single sequence
    argument, it returns a list of 1-tuples. With no arguments, it returns an
    empty list.

    The left-to-right evaluation order of the iterables is guaranteed. This
    makes possible an idiom for clustering a data series into n-length groups
    using zip(*[iter(s)]*n).

    zip() in conjunction with the * operator can be used to unzip a list: >>>

    >>> x = [1, 2, 3]
    >>> y = [4, 5, 6]
    >>> zipped = zip(x, y)
    >>> zipped
    [(1, 4), (2, 5), (3, 6)]
    >>> x2, y2 = zip(*zipped)
    >>> x == list(x2) and y == list(y2)
    True

enumerate - Iterate over indices and items of a list¶

The Python Cookbook (Recipe 4.4) describes how to iterate over items and indices
in a list using enumerate. For example:

alist = ['a1', 'a2', 'a3']

for i, a in enumerate(alist):
    print i, a

Results:

0 a1
1 a2
2 a3

zip - Iterate over two lists in parallel

I previously wrote about using zip to iterate over two lists in parallel.
Example:

alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']

for a, b in zip(alist, blist):
    print a, b

Results:

a1 b1
a2 b2
a3 b3

enumerate with zip

Here is how to iterate over two lists and their indices using enumerate together
with zip:

alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']

for i, (a, b) in enumerate(zip(alist, blist)):
    print i, a, b

Results:

0 a1 b1
1 a2 b2
2 a3 b3
