def sumDigits(number): 
    def calculate(x,y):
        return abs(int(x)) + int(y) if x is not '-' else x + y
    return reduce(calculate, list(str(number))) 
