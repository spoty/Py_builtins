In python, you can put 'j' after a number to make it imaginary.

complex()

Create a complex number with the value real + imag*j or convert a string or
number to a complex number. If the first parameter is a string, it will be
interpreted as a complex number and the function must be called without a second
parameter. The second parameter can never be a string. Each argument may be any
numeric type (including complex). If imag is omitted, it defaults to zero and
the function serves as a numeric conversion function like int(), long() and
float(). If both arguments are omitted, returns 0j.

Note

When converting from a string, the string must not contain whitespace around the
central + or - operator. For example, complex('1+2j') is fine, but complex('1 +
2j') raises ValueError.
