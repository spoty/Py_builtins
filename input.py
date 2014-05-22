"""
The difference is that raw_input() does not exist in Python 3.x,
while input() does. Actually, the old raw_input() has been
renamed to input(), and the old input() is gone (but can easily
be simulated by using eval(input())).


In Python 2, raw_input() returns a string, and input() tries to run the
input as a Python expression. Since getting a string was almost always
what you wanted, Python 3 does that with input()
"""

a = input()
