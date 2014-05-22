"""
The difference is that raw_input() does not exist in Python 3.x,
while input() does. Actually, the old raw_input() has been
renamed to input(), and the old input() is gone (but can easily
be simulated by using eval(input())).


In Python 2, raw_input() returns a string, and input() tries to run the
input as a Python expression. Since getting a string was almost always
what you wanted, Python 3 does that with input()
"""

# In python 2.x, raw_input() returns a string and input() evaluates
# the input in the execution context in which it is called

x = input()
#"hello"
y = input()
x + " world"
y
#'hello world'

# In python 3.x, input has been scrapped and the function previously
# known as raw_input is now input. So you have to manually call compile
# and than eval if you want the old functionality.

# python2.x                    python3.x

# raw_input()   --------------> input()
# input()  -------------------> eval(input())

# In 3.x, the above session goes like this

x = eval(input())
'hello'
y = eval(input())
x + ' world'
y
'hello world'
