pangram = "The quick, brown fox jumps over the lazy dog!"
import string

def is_pangram(s):
    all_letters = set([c for c in s.lower() if 'a' <= c <= 'z'])
    return len(all_letters) == 26




### another best example 
import string

def is_pangram(s):
    return set(string.lowercase) <= set(s.lower())
