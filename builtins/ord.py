"""
Some times it is require to convert a string to unicode ASCII value and
this inbuilt function will give python this capability.
"""

# Convert a char to its corresponding ascii value.
string = "Hello World"
list_ascii = [ord(i) for i in string]
print list_ascii

list_char = [chr(i) for i in list_ascii]
print ''.join(list_char)

