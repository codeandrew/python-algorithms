def dont_give_me_five(start,end):
    def take(data):
        return 'x' if '5' in str(data) else data
    list = map(take, range(start, end+1))
    return len(filter(lambda x : not x == 'x', list))
