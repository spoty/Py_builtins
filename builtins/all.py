"""
You can roughly think of any and all as logical OR and AND operators,
respectively.

any

any will return True when atleast one of the values is Truthy.
Read about Truth Value Testing.

all

all will return True only when all the elements are Truthy.

Truth table

                        any     all
-------------------------------------
All Truthy values      True    True
All Falsy values       False   False
Atleast one Truthy     True    False
Atleast one Falsy      True    False
"""

items = [[1, 2, 0], [1, 2, 0], [1, 2, 0]]
print all(item[2] == 0 for item in items)
# True
items = [[1, 2, 0], [1, 2, 1], [1, 2, 0]]
print all(item[2] == 0 for item in items)
# False

# And, for his filter example, a list comprehension:

print [x for x in items if x[2] == 0]
# [[1, 2, 0], [1, 2, 0]]

# If you want to check at least one element is 0, the better option
# is to use any() which is more readable:

print any(item[2] == 0 for item in items)
# True
