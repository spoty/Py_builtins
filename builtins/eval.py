"""
http://stackoverflow.com/questions/1087255/use-of-eval-in-python
http://lybniz2.sourceforge.net/safeeval.html
http://nedbatchelder.com/blog/201206/eval_really_is_dangerous.html
http://www.floyd.ch/?p=584
http://vipulchaskar.blogspot.de/2012/10/exploiting-eval-function-in-python.html

The eval function lets a python program run python code within itself.
eval example (interactive shell):
"""
x = 1
eval('x + 1')
# 2
eval('x')
# 1


print eval("__import__('os').getcwd()")

# quick JSON parser example
r='''
{
    "glossary": {
        "title": "example glossary"
        }
}
'''

print eval(r)['glossary']['title']


from math import *
user_func = raw_input("type a function: y = ")
for x in range(1,10): print "x = ", x , ", y = ", eval(user_func)

# The user can type in an expression and it gets evaluated with different values of x.

# type a function: y = sin(x/20.0)
