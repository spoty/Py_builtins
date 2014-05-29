
hasattr(object, name)

    The arguments are an object and a string. The result is True if the string
    is the name of one of the object’s attributes, False if not. (This is
    implemented by calling getattr(object, name) and seeing whether it raises an
    exception or not.)


hasattr internally and rapidly performs the same task as the try/except block:
it's a very specific, optimized, one-task tool and thus should be preferred,
when applicable, to the very general-purpose alternative.




As Jarret Hardie answered, hasattr will do the trick. I would like to add,
though, that many in the Python community recommend a strategy of "easier to ask
for forgiveness than permission" (EAFP) rather than "look before you leap"
(LBYL). See these references:

EAFP vs LBYL (was Re: A little disappointed so far) EAFP vs. LBYL @Code Like a
Pythonista: Idiomatic Python

ie:

try:
    doStuff(a.property)
except AttributeError:
    otherStuff()

... is preferred to:

if hasattr(a, 'property'):
    doStuff(a.property)
else:
    otherStuff()

