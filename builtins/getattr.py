"""  Return the value of the named attribute of object. name must be a string.
If the string is the name of one of the object’s attributes, the result is the
value of that attribute. For example, getattr(x, 'foobar') is equivalent to
x.foobar. If the named attribute does not exist, default is returned if
provided, otherwise AttributeError is raised.
"""
class Person():
    name = 'Victor'
    def say(self, what):
        print(self.name, what)

attr_name = 'name'
person = Person()
getattr(person, attr_name)
# 'Victor'
getattr(person, 'say')('Hello')
# Victor Hello

"""
Used in:
- Introspection


ome basics first:

With objects, you need to deal with its attributes. Ordinarily we do
instance.attribute. Some times we need more control (when we do not know the name
of attribute in advance)

instance.attribute would become getattr(instance, attribute_name)

Using this model we can get the attribute by supplying the attribute_name. This
works when we give a name as a string and you need to look up the instance
attribute referenced by that name.

Use of __getattr__
You can also tell a class how to deal with attributes it doesn’t explicitly
manage and do that via __getattr__ method

Python will call it whenever you request an attribute that hasn’t already been
defined. So you can define what to do with it. A classic usecase:

class A(dict):     def __getattr__(self, name):        return self[name] a = A()
# Now a.somekey will give a['somekey']

Caveats and use of __getattribute__

If you need to catch every attribute regardless whether it exists or not, use
__getattribute__ instead. Difference

__getattr__ only gets called for attributes that don’t actually exist. If you
set the attribute directly, referencing that attribute will retrieve it without
calling __getattr__.

__getattribute__ is called all the times.
"""
