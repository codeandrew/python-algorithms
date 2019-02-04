def find_missing_letter(chars):
    letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    upperCaseLetter = letters.upper()

    l = letters.strip().split(" ")
    uL = upperCaseLetter.strip().split(" ")

    def search(list):
        start = list.index(chars[0])
        items = list[slice(start , len(chars))]
        print items, start, len(chars)
        for key in items:
            if key in chars :  print key
            else : return key

    if chars[0] in l : return search(l)
    else : return search(uL)


test.assert_equals(find_missing_letter(['a','b','c','d','f']), 'e')
test.assert_equals(find_missing_letter(['O','Q','R','S']), 'P')
