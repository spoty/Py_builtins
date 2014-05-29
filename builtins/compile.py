It is not that commonly used. It is used when you have Python source code in
string form, and you want to make it into a Python code object that you can keep
and use. Here's a trivial example:

>>> codeobj = compile('x = 2\nprint "X is", x', 'fakemodule', 'exec') >>>
exec(codeobj) X is 2

Basically, the code object converts a string into an object that you can later
call exec on to run the source code in the string. (This is for "exec" mode; the
"eval" mode allows use of eval instead, if the string contains code for a single
expression.) This is not a common task, which is why you may never run across a
need for it.

The main use for it is in metaprogramming or embedding situations. For instance,
if you have a Python program that allows users to script its behavior with
custom Python code, you might use compile and exec to store and execute these
user-defined scripts.

Another reason compile is rarely used is that, like exec, eval, and their ilk,
compile is a potential security hole. If you take user code in string form and
compile it and later exec it, you could be running unsafe code. (For instance,
imagine that in my example above the code was formatYourHardDrive() instead of
print x.)
