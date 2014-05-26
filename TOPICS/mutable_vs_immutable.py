""" You have to understand that Python represents all its data as objects. Some
of these objects like lists and dictionaries are mutable, meaning you can change
their content without changing their identity. Other objects like integers,
floats, strings and tuples ... are objects that can not be changed. An easy way
to understand that is if you have a look at an objects ID.
http://stackoverflow.com/questions/8056130/immutable-vs-mutable-types-python

Immutable:

    integers and other numerical types string types like str and unicode tuples

Mutable: everything else, like,

    lists dicts classes class instances etc.

And id()method is good way to tell. For example"""

# For an integer:

n = 1 id(n) # **704 n = n + 1 n # 2 id(n) # **736

# For a list:

m = [1] id(m) #**416 m.append(2) m #[1, 2] id(m) #**416

