"""
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
"""


# My Solution
def unique_in_order(iterable):
    new = []
    for i in iterable:
        if len(new) < 1 or not i == new[len(new) - 1]:
            new.append(i)
            
    return new
    
    
# CLEVER 
def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result
# This logic is add the element then check if it's already added
  
  
  
# CLEVER 2
def unique_in_order(iterable):
    r = []
    for x in iterable:
        x in r[-1:] or r.append(x)
    return r

"""
NOTES:


>>> l = []
>>> len(l)
0
>>> l[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range


Checking of index that's out of range you can use "OR"

>>> if 1 or not l[0]:
...     2
...
2


tags:
checking next element of list or array
"""
