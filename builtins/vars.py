vars() and locals()

Now, to answer another part of your question. vars() (or locals()) provides low
level access to variables created by python. Thus the following two lines are
equivalent.

locals()['x'] = 4 x = 4

The scope of vars()['x'] is exactly the same as the scope of x. One problem with
locals() (or vars()) is that it will let you put stuff in the namespace that you
can't get out of the namespace by normal means. So you can do something like
this: locals()[4] = 'An integer', but you can't get that back out without using
locals again, because the local namespace (as with all python namespaces) is
only meant to hold strings.

>>> x = 5 >>> dir() ['__builtins__', '__doc__', '__name__', 'x'] >>> locals()[4]
= 'An integer' >>> dir() [4, '__builtins__', '__doc__', '__name__', 'x'] >>> x 5
>>> 4 4 >>> locals()[4] 'An integer'

Note that 4 does not return the same thing as locals()[4]. This can lead to some
unexpected, difficult to debug problems. This is one reason to avoid using
locals(). Another is that it's generally a lot of complication just to do things
that python provides simpler, less error prone ways of doing (like creating a
sequence of variables).
