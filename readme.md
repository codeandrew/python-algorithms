# Python Algorithms
> for practicing python



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

Extract number from strings
```python
string = "Hello 12345 World "
numbers = [x for x in string if x.isdigit()]
print(numbers) # Output  ['1', '2', '3', '4', '5']
```
