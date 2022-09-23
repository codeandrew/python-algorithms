"""
Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel.
"""


# My Solution
def disemvowel(string):
    x ="aeiouAEIOU"
    for i in string: 
        if i in x: 
            string = string.replace(i, "")
            
    return string


# CLEVER 
def disemvowel(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s




# OLD SOLUTIONS 2019
def disemvowel(string):
    vowel = "a e i o u A E I O U".strip().split(" ")
    arr = list(string)
    for i in arr:
        if ( i in vowel ):
            arr.remove(i)

    return ''.join(arr)


def disemvowel(s):
    vowel = "a e i o u",strip().split(" ")
    list = list(string.lower())
    return ''.join([list.remove(i) for i in list if i in vowel])
