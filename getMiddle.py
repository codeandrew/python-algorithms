def get_middle(str):
    if len(str) > 2:
        if len(str) % 2 == 0:
            x = round(len(str)/2)
            return str[int(x-1):int(x+1)]
        else:
            return str[int(len(str)/2)]
        pass
    else:
        return str


---

def get_middle(s):
    index, odd = divmod(len(s), 2)
    return s[index] if odd else s[index - 1:index + 1]
