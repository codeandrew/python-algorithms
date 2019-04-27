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
