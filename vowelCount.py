def getCount(inputStr):
    vowels = 'a e i o u'.strip().split(' ')
    def counter(string):
        if string in vowels:  return 1
        else : return 0

    numbers = map(counter, inputStr)
    return reduce((lambda x, y: x + y), numbers)
