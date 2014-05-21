"""
divmod(a, b)

Takes two (non complex) numbers as arguments and return a pair of numbers
consisting of their quotient and remainder when using long division.
With mixed operand types, the rules for binary arithmetic operators apply.
For plain and long integers, the result is the same as (a // b, a % b).
For floating point numbers the result is (q, a % b), where q is usually
math.floor(a / b) but may be 1 less than that. In any case q * b + a % b
is very close to a, if a % b is non-zero it has the same sign as b, and
0 <= abs(a % b) < abs(b).

Returns: quotient and the modulo
"""

seconds = 137
minutes, seconds = divmod(seconds, 60)

print minutes, seconds

"""
/ and //

In Python 3.0, 5 / 2 will return 2.5 and 5 // 2 will return 2.
The former is floating point division, and the latter is floor division,
 sometimes also called integer division.

In Python 2.2 or later in the 2.x line, there is no difference
for integers unless you perform a from __future__ import division,
which causes Python 2.x to adopt the behavior of 3.0

Regardless of the future import, 5.0 // 2 will return 2.0 since that's the
floor division result of the operation.
"""
