"""
Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

Examples

"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
"""

# My Solution
def reverse_words(text):
    rev = ''.join(list(text)[::-1])
    return " ".join(rev.split(' ')[::-1])
    


   
  
# Cleaner
def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))
