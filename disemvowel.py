def disemvowel(string):
    vowel = "a e i o u A E I O U".strip().split(" ")
    arr = list(string)
    for i in arr:
        if ( i in vowel ):
            arr.remove(i)

    return ''.join(arr)
