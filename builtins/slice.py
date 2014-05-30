You create a slice by calling slice with the same fields you would use if doing [start:end:step] notation:

sl = slice(0,4)

To use the slice, just pass it as if it were the index into a list or string:

>>> s = "ABCDEFGHIJKL"
>>> sl = slice(0,4)
>>> print s[sl]
'ABCD'

Let's say you have a file of fixed-length text fields. You could define a list
of slices to easily extract the values from each "record" in this file.

data = """\
0010GEORGE JETSON    12345 SPACESHIP ST   HOUSTON       TX
0020WILE E COYOTE    312 ACME BLVD        TUCSON        AZ
0030FRED FLINTSTONE  246 GRANITE LANE     BEDROCK       CA
0040JONNY QUEST      31416 SCIENCE AVE    PALO ALTO     CA""".splitlines()


fieldslices = [slice(*fielddef) for fielddef in [
    (0,4), (4, 21), (21,42), (42,56), (56,58),
    ]]
fields = "id name address city state".split()

for rec in data:
    for field,sl in zip(fields, fieldslices):
        print field, ':', rec[sl]
    print

Prints:

id : 0010
name : GEORGE JETSON
address : 12345 SPACESHIP ST
city : HOUSTON
state : TX

id : 0020
name : WILE E COYOTE
address : 312 ACME BLVD
city : TUCSON
state : AZ

id : 0030
name : FRED FLINTSTONE
address : 246 GRANITE LANE
city : BEDROCK
state : CA

id : 0040
name : JONNY QUEST
address : 31416 SCIENCE AVE
city : PALO ALTO
state : CA

