def accum(s):
    return "-".join([ ((index+1) * item).title() for index, item in enumerate(s)])
