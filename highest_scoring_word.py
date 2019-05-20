"""
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
"""


def high(x):
    l = x.strip(" ").split()
    s = []
    for i in l:
        ss =[]
        s.append(ss)
        for ii in i:
            ss.append(ord(ii)-96)

    sumList = [sum(i) for i in s]
    return l[sumList.index(max(sumList))]


"""
Other Options
"""

def high(x):
    words=x.split(' ')
    list = []
    for i in words:
        scores = [sum([ord(char) - 96 for char in i])]
        list.append(scores)
    return words[list.index(max(list))]


def high(words):
    return max(words.split(), key=lambda word: sum(ord(c) - ord('a') + 1 for c in word.lower()))
