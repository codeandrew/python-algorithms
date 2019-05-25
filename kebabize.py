"""
Modify the kebabize function so that it converts a camel case string into a kebab case.

kebabize('camelsHaveThreeHumps') // camels-have-three-humps
kebabize('camelsHave3Humps') // camels-have-humps
Notes:

the returned string should only contain lowercase letters
"""

def kebabize(string):
    ns= []
    for a in string:
        if a.islower(): ns.append(a)
        elif a.isupper():
            ns.append("-")
            ns.append(a.lower())
    return ("".join(ns)).strip("-")


"""
Other solutions
"""


def kebabize(s):
    return ''.join(c if c.islower() else '-' + c.lower() for c in s if c.isalpha()).strip('-')



import re
def kebabize(s):
    s = ''.join([i for i in s if not i.isdigit()])
    kebablist = filter(None, re.split("([A-Z][^A-Z]*)", s))
    return "-".join(x.lower() for x in kebablist)



