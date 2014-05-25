
# pow(x, y[, z])

"""
    Return x to the power y; if z is present, return x to the power y, modulo z
    (computed more efficiently than pow(x, y) % z). The two-argument form pow(x,
    y) is equivalent to using the power operator: x**y.

    The arguments must have numeric types. With mixed operand types, the
    coercion rules for binary arithmetic operators apply. For int and long int
    operands, the result has the same type as the operands (after coercion)
    unless the second argument is negative; in that case, all arguments are
    converted to float and a float result is delivered. For example, 10**2
    returns 100, but 10**-2 returns 0.01. (This last feature was added in Python
    2.2. In Python 2.1 and before, if both arguments were of integer types and
    the second argument was negative, an exception was raised.) If the second
    argument is negative, the third argument must be omitted. If z is present, x
    and y must be of integer types, and y must be non-negative. (This
    restriction was added in Python 2.2. In Python 2.1 and before, floating
    3-argument pow() returned platform-dependent results depending on floating-
    point rounding accidents.)


So, while pow and math.pow are about twice as slow, they are still fast enough
to not care much. Unless you can actually identify the exponentiation as a
bottleneck, there won’t be a reason to choose one method over the other if
clarity decreases. This especially applies since pow offers an integrated modulo
operation for example.

What's the diffreence ** and pow

The big difference of math.pow to both the builtin pow and the power operator **
is that it always uses float semantics. So if you, for some reason, want to make
sure you get a float as a result back, then math.pow will ensure this property.

Let’s think of an example: We have two numbers, i and j, and have no idea if
they are floats or integers. But we want to have a float result of i^j. So what
options do we have?

    We can convert at least one of the arguments to a float and then do i ** j.

    We can do i ** j and convert the result to a float (float exponentation is
    automatically used when either i or j are floats, so the result is the
    same).

    We can use math.pow.

http://stackoverflow.com/questions/10282674/difference-between-the-built-in-pow-and-math-pow-for-floats-in-python
"""
