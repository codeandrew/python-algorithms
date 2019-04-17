def sort_array(s):
    print(s)
    odd = [ i for i in s if i % 2 != 0 ]
    even = [ i  if i % 2 == 0 else 0 for i in s ]
    odd.sort()
    print(odd)
    print(even, "even")
    #answer = [ odd[k - 1] if i is 0 else i for k,i in enumerate(even) ]
    answer = [  i if i is not 0 else odd.popleft() for i in even ]
    answer = [  i if i in even not 0 else odd.popleft() for i in odd ]

    print(answer)
    return answer

"""
You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

Example

sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python

    out = sorted(s, key = lambda n:(n%2, n))
"""
