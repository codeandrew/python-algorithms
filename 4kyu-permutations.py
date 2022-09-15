"""
In this kata you have to create all permutations of a non empty input string and remove duplicates, if present. This means, you have to shuffle all letters from the input in all possible orders.

Examples:

* With input 'a'
* Your function should return: ['a']
* With input 'ab'
* Your function should return ['ab', 'ba']
* With input 'aabb'
* Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
The order of the permutations doesn't matter.

"""

# my first solution, working but too slow
def permutation(item):
    print(item)
    if len(item) == 1: return [item]

    l = []
    for i in range(len(item)):
        m = item[i]
        remaining_item = item[:i] + item[i+1:]

        [l.append([m] + p) for p in permutation(remaining_item) if]

    return l

def permutations(s):
    new = []
    for i in permutation(list(s)):
        new_string =  "".join(i)
        new.append(new_string)
        
        if new_string not in new:
            new.append(new_string)
    
    return new
  
  
# My Second Solution, working and fast enough to be submitted
def permute(word):
    if len(word) == 1:
        return [word]
    permutations = permute(word[1:])
    character = word[0]
    result = []
    for p in permutations:
        for i in range(len(p)+1):
            new = p[:i] + character + p[i:]
            if new not in result:
                result.append(new)
                
    return result 

def permutations(s):
    return permute(s)

"""
OTHER PEOPLE SOLUTION
"""
# CLEVER 
def permutations(s):        
    if(len(s)==1): return [s]
    result=[]
    for i,v in enumerate(s):
        result += [v+p for p in permutations(s[:i]+s[i+1:])]
    return list(set(result))

  
# USING itertools
import itertools

def permutations(string):
    return list("".join(p) for p in set(itertools.permutations(string)))
