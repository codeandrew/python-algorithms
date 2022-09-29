"""
Complete the solution so that the function will break up camel casing, using a space between words.

Example

"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
"""

# MY Solution
def solution(s):
    index_list = [k for k,v in enumerate(s) if v.isupper()]
    l = list(s)
    counter = 0
    for i in index_list:
        l.insert(i + counter, " ")
        counter += 1
        
    return "".join(l)
     

# CLEVER 
import re
def solution(s):
    return re.sub('([A-Z])', r' \1', s)

  
# CLEAN and Clever 
def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)
