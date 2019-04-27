test.assert_equals(highest_same_number([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)

def highest_same_number(seq):
    d = {x:seq.count(x) for x in seq}
    return d.keys()[d.values().index(max(d.values()))]

    """
    1. filter the sequence into a dictonary
    2. get the highest value
    3. get the index of the value
    4. return the key of the highest value in the dictonary
    """
