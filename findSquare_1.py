import math

def is_square(n): 
    if n == 0 : return True
    try :
        root = math.sqrt(n)
        return True if n % root == 0 else False
    except :
        return False

