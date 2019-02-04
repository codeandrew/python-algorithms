def expanded_form(num):
    rev = str(num)[::-1]
    list = [value + '0' * key for key, value in enumerate(rev) if value > '0']
    return ' + '.join(list[::-1])
