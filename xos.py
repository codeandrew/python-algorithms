"""
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
"""
def xo(s):
    if 'x' not in s and 'o' not in s : return True
    x = filter(lambda a: a == 'x', s.lower())
    o = filter(lambda a: a == 'o', s.lower())
    return True if len(x) == len(o) else False

"""
Best Practices
"""
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')
