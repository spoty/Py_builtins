bytearray()

A bytearray is very similar to a regular python string (str in python2.x, bytes
in python3) but with an important difference, whereas strings are immutable,
bytearrays are mutable, a bit like a list of single character strings.

This is useful because some applications use byte sequences in ways that perform
poorly with immutable strings. When you are making lots of little changes in the
middle of large chunks of memory, as in a database engine, or image library,
strings perform quite poorly; since you have to make a copy of the whole
(possibly large) string. bytearrays have the advantage of making it possible to
make that kind of change without making a copy of the memory first.

But this particular case is actually more the exception, rather than the rule.
Most uses involve comparing strings, or string formatting. For the latter,
there's usually a copy anyway, so a mutable type would offer no advantage, and
for the former, since immutable strings cannot change, you can calculate a hash
of the string and compare that as a shortcut to comparing each byte in order,
which is almost always a big win; and so it's the immutable type (str or bytes)
that is the default; and bytearray is the exception when you need it's special
features.


===============================================================================
Example 1: Assembling a message from fragments

Suppose you're writing some network code that is receiving a large message on a
socket connection. If you know about sockets, you know that the recv() operation
doesn't wait for all of the data to arrive. Instead, it merely returns what's
currently available in the system buffers. Therefore, to get all of the data,
you might write code that looks like this:

# remaining = number of bytes being received (determined already)
msg = b""
while remaining > 0:
    chunk = s.recv(remaining)    # Get available data
    msg += chunk                 # Add it to the message
    remaining -= len(chunk)

The only problem with this code is that concatenation (+=) has horrible
performance. Therefore, a common performance optimization in Python 2 is to
collect all of the chunks in a list and perform a join when you're done. Like
this:

# remaining = number of bytes being received (determined already)
msgparts = []
while remaining > 0:
    chunk = s.recv(remaining)    # Get available data
    msgparts.append(chunk)       # Add it to list of chunks
    remaining -= len(chunk)
msg = b"".join(msgparts)          # Make the final message

Now, here's a third solution using a bytearray:

# remaining = number of bytes being received (determined already)
msg = bytearray()
while remaining > 0:
    chunk = s.recv(remaining)    # Get available data
    msg.extend(chunk)            # Add to message
    remaining -= len(chunk)

Notice how the bytearray version is really clean. You don't collect parts in a
list and you don't perform that cryptic join at the end. Nice.

Of course, the big question is whether or not it performs. To test this out, I
first made a list of small byte fragments like this:

chunks = [b"x"*16]*512

I then used the timeit module to compare the following two code fragments:

# Version 1
msgparts = []
for chunk in chunks:
    msgparts.append(chunk)
msg = b"".join(msgparts)

#Version 2
msg = bytearray()
for chunk in chunks:
    msg.extend(chunk)

When tested, version 1 of the code ran in 99.8s whereas version 2 ran in 116.6s
(a version using += concatenation takes 230.3s by comparison). So while
performing a join operation is still faster, it's only faster by about 16%.
Personally, I think the cleaner programming of the bytearray version might make
up for it. Example 2: Binary record packing

This example is an slight twist on the last example. Support you had a large
Python list of integer (x,y) coordinates. Something like this: points =
[(1,2),(3,4),(9,10),(23,14),(50,90),...] Now, suppose you need to write that
data out as a binary encoded file consisting of a 32-bit integer length followed
by each point packed into a pair of 32-bit integers. One way to do it would be
to use the struct module like this:

import struct
f = open("points.bin","wb")
f.write(struct.pack("I",len(points)))
for x,y in points:
    f.write(struct.pack("II",x,y))
f.close()

The only problem with this code is that it performs a large number of small
write() operations. An alternative approach is to pack everything into a
bytearray and only perform one write at the end. For example:

import struct
f = open("points.bin","wb")
msg = bytearray()
msg.extend(struct.pack("I",len(points))
for x,y in points:
    msg.extend(struct.pack("II",x,y))
f.write(msg)
f.close()

Sure enough, the version that uses bytearray runs much faster. In a simple
timing test involving a list of 100000 points, it runs in about half the time as
the version that makes a lot of small writes. Example 3: Mathematical processing
of byte values

The fact that bytearrays present themselves as arrays of integers makes it
easier to perform certain kinds of calculations. In a recent embedded systems
project, I was using Python to communicate with a device over a serial port. As
part of the communications protocol, all messages had to be signed with a
Longitudinal Redundancy Check (LRC) byte. An LRC is computed by taking an XOR
across all of the byte values. Bytearrays make such calculations easy. Here's
one version:

message = bytearray(...)     # Message already created
lrc = 0
for b in message:
    lrc ^= b
message.append(lrc)          # Add to the end of the message

Here's a version that increases your job security:
message.append(functools.reduce(lambda x,y:x^y,message)) And here's the same
calculation in Python 2 without bytearrays:

message = "..."       # Message already created
lrc = 0
for b in message:
    lrc ^= ord(b)
message += chr(lrc)        # Add the LRC byte

Personally, I like the bytearray version. There's no need to use ord() and you
can just append the result at the end of the message instead of using
concatenation.

Here's another cute example. Suppose you wanted to run a bytearray through a
simple XOR-cipher. Here's a one-liner to do it:

>>> key = 37
>>> message = bytearray(b"Hello World")
>>> s = bytearray(x ^ key for x in message)
>>> s
bytearray(b'm@IIJ\x05rJWIA')
>>> bytearray(x ^ key for x in s)
bytearray(b"Hello World")
>>>

Here is a link to the presentation
