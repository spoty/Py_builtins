
memoryview(obj)

    Return a “memory view” object created from the given argument. See
    memoryview type for more information.


>>> v = memoryview('abcefg')
>>> v[1]
'b'
>>> v[-1]
'g'
>>> v[1:4]
<memory at 0x77ab28>
>>> v[1:4].tobytes()
'bce'
