
The object returned by range() is known as a generator.

Instead of storing the entire range, [0,1,2,..,9], in memory, the generator
stores a definition for (i=0; i<10; i+=1) and computes the next value only when
needed (AKA lazy-evaluation).

Essentially, a generator allows you to return a list like structure, but here
are some differences:

    A list stores all elements when it is created. A generator generates the
    next element when it is needed.
    A list can be iterated over as much as you
    need, a generator can only be iterated over exactly once.
    A list can get
    elements by index, a generator cannot -- it only generates values once, from
    start to end.

A generator can be created in two ways:

(1) Very similar to a list comprehension:

# this is a list, create all 5000000 x/2 values immediately, uses []
lis = [x/2 for x in range(5000000)]

# this is a generator, creates each x/2 value only when it is needed, uses ()
gen = (x/2 for x in range(5000000))

(2) As a function, using yield to return the next value:

# this is also a generator, it will run until a yield occurs, and return that result.
# on the next call it picks up where it left off and continues until a yield occurs...
def divby2(n):
    num = 0
    while num < n:
        yield num/2
        num += 1

# same as (x/2 for x in range(5000000))
print divby2(5000000)

Note:
Even though range(5000000) is a generator in Python3.x, [x/2 for x in
range(5000000)] is still a list. range(...) does it's job and generates x one at
a time, but the entire list of x/2 values will be computed when this list is
create.
