""" bin(x)

    Convert an integer number to a binary string. The result is a valid Python
    expression. If x is not a Python int object, it has to define an __index__()
    method that returns an integer.
"""

print bin(30)[2:].zfill(8)
print "{0:b}".format(10)


