"""
Two tortoises named A and B must run a race. A starts with an average speed of 720 feet per hour. Young B knows she runs faster than A, and furthermore has not finished her cabbage.

When she starts, at last, she can see that A has a 70 feet lead but B's speed is 850 feet per hour. How long will it take B to catch A?

More generally: given two speeds v1 (A's speed, integer > 0) and v2 (B's speed, integer > 0) and a lead g (integer > 0) how long will it take B to catch A?

The result will be an array [hour, min, sec] which is the time needed in hours, minutes and seconds (round down to the nearest second) or a string in some languages.

If v1 >= v2 then return nil, nothing, null, None or {-1, -1, -1} for C++, C, Go, Nim, Pascal, COBOL, Erlang, [-1, -1, -1] for Perl,[] for Kotlin or "-1 -1 -1".

Examples:
(form of the result depends on the language)

race(720, 850, 70) => [0, 32, 18] or "0 32 18"
race(80, 91, 37)   => [3, 21, 49] or "3 21 49"
Note:
See other examples in "Your test cases".

In Fortran - as in any other language - the returned string is not permitted to contain any redundant trailing whitespace: you can use dynamically allocated character strings.

** Hints for people who don't know how to convert to hours, minutes, seconds:

Tortoises don't care about fractions of seconds
Think of calculation by hand using only integers (in your code use or simulate integer division)
or Google: "convert decimal time to hours minutes seconds"
"""

# My Solution
def race(v1, v2, g):
    if v1 >= v2 : return None
    t = float(g)/(v2-v1)*3600
    mn, s = divmod(t, 60)
    h, mn = divmod(mn, 60)
    
    return [int(h), int(mn), int(s)]
    


# Solution with datetime library
from datetime import datetime, timedelta

def race(v1, v2, g):
    if v1 >= v2:
        return None
    else:
        sec = timedelta(seconds=int((g*3600/(v2-v1))))
        d = datetime(1,1,1) + sec
        
        return [d.hour, d.minute, d.second]

# Using Math Library 
import math

def race(v1, v2, g):
    # your code
    if v1 > v2:
        return None
    speedDiff = v2-v1;
    totalSec = g/(speedDiff/3600)
    s = math.floor(totalSec%60)
    m = math.floor((totalSec%3600)/60)
    h = math.floor(totalSec/3600)
    
    return [h,m,s]
    

      
# Clever 
def race(v1, v2, g):
    t = 3600 * g/(v2-v1)
    return [t/3600, t/60%60, t%60] if v2 > v1 else None

# Clever 2
def race(v1, v2, g):
    if v2 <= v1:
        return None
    total = g / (v2 - v1)
    return [int(total), int(total * 60) % 60, int(total * 3600) % 60]

# Clever 3 
def race(v1, v2, g):
    if v1 < v2:
        a = g * 3600 // (v2 - v1)
        return [a // 3600, a // 60 % 60, a % 60]

