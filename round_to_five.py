def round_to_next5(n):
    roundingList = map(int, range(-100, 101, 5))
    if n in roundingList : return n
    for i in roundingList:
        if n < i : return i


##
# best practice
##
def round_to_next5(n):
    return n + (5 - n) % 5
