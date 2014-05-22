# Introducing str
import math
# 1
str(1)
horsemen = ['war', 'pestilence', 'famine']
print horsemen
#['war', 'pestilence', 'famine']
horsemen.append('Powerbuilder')
# 2
str(horsemen)
#"['war', 'pestilence', 'famine', 'Powerbuilder']"
# 3
str(math)
# <module 'math' <built-in>>
str(None)
#'None'

"""
1   For simple datatypes like integers, you would expect str to work,
    because almost every language has a function to convert an integer
    to a string.
2   However, str works on any object of any type. Here it works on a list
    which you've constructed in bits and pieces.
3   str also works on modules. Note that the string representation of the
    module includes the pathname of the module on disk, so yours will
    be different.
4   A subtle but important behavior of str is that it works on None,
    the Python null value. It returns the string 'None'. You'll use this
     to your advantage in the info function, as you'll see shortly.
"""
