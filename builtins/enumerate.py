"""
[(i, j) for i, j in enumerate(mylist)]

You need to put i,j inside a tuple for the list comprehension to work.
 Alternatively, given that enumerate() already returns a tuple, you can
  return it directly without unpacking it first:

[pair for pair in enumerate(mylist)]

Either way, the result that gets returned is as expected:

> [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]
"""

mylist = ["a", "b", "c", "d"]

print[(i, j) for i, j in enumerate(mylist)]
# or
print[pair for pair in enumerate(mylist)]
# or
print list(enumerate(mylist))
