"""
Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.

Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.

"""
#MY SOLUTION
def lovefunc( f1, f2 ):
    is_even = lambda a: 1 if (a % 2) == 0 else  0
    
    one = is_even(f1)
    two = is_even(f2)
    return one == 1 and two == 0 or one == 0 and two == 1
    
    
    
    
    
    
def lovefunc( flower1, flower2 ):
    return (flower1+flower2)%2

def lovefunc(flower1, flower2):
    return flower1 % 2 != flower2 % 2
