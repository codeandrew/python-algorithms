def alphabet_position(text):
    alpha = "a b c d e f g h i j k l m n o p q r s t u v w x y z".strip().split(' ')

    filtered = [str(index+1) for s in text.lower() for index, letter in enumerate(alpha) if letter == s]
    return ' '.join(filtered)



def normal_way(text)
    fil = []
    alpha = "a b c d e f g h i j k l m n o p q r s t u v w x y z".strip().split(' ')
    for s in text.lower():
        for index, letter in enumerate(alpha):
            if letter == s : fil.append(index+1)
    pass



"""
other ways
"""
def alphabet_position(text):
    al = "abcdefghijklmnopqrstuvwxyz"
    return " ".join([str(al.index(l)+1) for l in text if l.isalpha()])
