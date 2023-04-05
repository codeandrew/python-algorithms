# Python Algorithms
> for practicing python

## Coding Philosophies
You aren’t meant to master a Programming Language in the beginning.
You’re meant to go build them 

You don’t master a programming concept, 
you apply them in numerous project.
then you continuously improve on them

### SOLID


## Strings

### Unicodes
using `ord()` returns an integer representing the Unicode character
```
character = 'P'

# find unicode of P
unicode_char = ord(character)
print(unicode_char)

# Output: 80
```


The `chr()` method converts an integer to its unicode character and returns it.
```
print(chr(97))
# Output: a

print(chr(98))
#  Output: b
```



## Array Slicing 

```
a[start:stop]  # items start through stop-1
a[start:]      # items start through the rest of the array
a[:stop]       # items from the beginning through stop-1
a[:]           # a copy of the whole array
```

There is also the step value, which can be used with any of the above:

```
a[start:stop:step] # start through not past stop, by step
```

The key point to remember is that the :stop value represents the first value that is not in the selected slice. So, the difference between stop and start is the number of elements selected (if step is 1, the default).

The other feature is that start or stop may be a negative number, which means it counts from the end of the array instead of the beginning. So:

```
a[-1]    # last item in the array
a[-2:]   # last two items in the array
a[:-2]   # everything except the last two items
```

Similarly, step may be a negative number:

```
a[::-1]    # all items in the array, reversed
a[1::-1]   # the first two items, reversed
a[:-3:-1]  # the last two items, reversed
a[-3::-1]  # everything except the last two items, reversed
```

Python is kind to the programmer if there are fewer items than you ask for. For example, if you ask for a[:-2] and a only contains one element, you get an empty list instead of an error. Sometimes you would prefer the error, so you have to be aware that this may happen.

** Relationship with the slice object **. 

A slice object can represent a slicing operation, i.e.:

```
a[start:stop:step]
```

is equivalent to:

```
a[slice(start, stop, step)]
```

Slice objects also behave slightly differently depending on the number of arguments, similarly to `range()`, i.e. both `slice(stop)` and `slice(start, stop[, step])` are supported. To skip specifying a given argument, one might use None, so that e.g. `a[start:]` is equivalent to `a[slice(start, None)]` or `a[::-1]` is equivalent to `a[slice(None, None, -1)]`.




> more reference at: https://stackoverflow.com/questions/509211/understanding-slicing

## List Comprehensions

** Basic syntax: **  

``` Python
new_list = [expression for_loop_one_or_more conditions ]
```

Example:

Find squares of a number using for loop.

``` python
numbers = [1, 2, 3, 4]
squares = []

for n in numbers:
  squares.append(n**2)

print(squares)  # Output: [1, 4, 9, 16]
```


Finding squares using list comprehensions  
``` python
numbers = [1, 2, 3, 4]
squares = [n**2 for n in numbers]

print(squares)  # Output: [1, 4, 9, 16]
```

#### List comprehension more complex example

 Find common numbers from two list using for loop.   

 Normal way :
``` python
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]

common_num = []

for a in list_a:
  for b in list_b:
    if a == b:
      common_num.append(a)

print(common_num)  # Output [2, 3, 4]
```

List Comprehension:  
``` Python
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]

common_num = [a for a in list_a for b in list_b if a == b]

print(common_num) # Output: [2, 3, 4]
```

List comprehensions can also be used to iterate over strings as shown below:

``` python
list_a = ["Hello", "World", "In", "Python"]

small_list_a = [str.lower() for str in list_a]

print(small_list_a) # Output: ['hello', 'world', 'in', 'python']
```

List comprehension with IF only
```python
a = ["a","A","b", "B"]
b = [i for i in a if i.islower() ]
print(b)
# [ "a", "b"] 
```

List comprehension with IF ELSE 
```python
a = ["a","A","b", "B"]
b = [i if i.islower() else 0 for i in a  ]
print(b)
# [ "a", 0, "b", 0] 
```

Extract number from strings
```python
string = "Hello 12345 World "
numbers = [x for x in string if x.isdigit()]
print(numbers) # Output  ['1', '2', '3', '4', '5']
```


## MATH Operators

### Division 


/ → Floating point division

// → Floor division


Let’s see some examples in both Python 2.7 and in Python 3.5.

Python 2.7.10 vs. Python 3.5
```
print (2/3)  ----> 0                   Python 2.7
print (2/3)  ----> 0.6666666666666666  Python 3.5
```
Python 2.7.10 vs. Python 3.5
```
print (4/2)  ----> 2         Python 2.7
print (4/2)  ----> 2.0       Python 3.5
```
Now if you want to have (in Python 2.7) the same output as in Python 3.5, you can do the following:

Python 2.7.10
```
from __future__ import division
print (2/3)  ----> 0.6666666666666666   # Python 2.7
print (4/2)  ----> 2.0                  # Python 2.7
```
Whereas there isn't any difference between floor division in both Python 2.7 and in Python 3.5.
```
138.93//3 ---> 46.0        # Python 2.7
138.93//3 ---> 46.0        # Python 3.5
4//3      ---> 1           # Python 2.7
4//3      ---> 1           # Python 3.5
```
