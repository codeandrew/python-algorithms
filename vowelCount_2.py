# Best Practice - 328
def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")

## Best Practice - 118
def getCount(s):
    return sum(c in 'aeiou' for c in s)
