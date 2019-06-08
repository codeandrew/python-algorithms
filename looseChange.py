"""
Welcome young Jedi! In this Kata you must create a function that takes an amount of US currency in cents, and returns a dictionary/hash which shows the least amount of coins used to make up that amount. The only coin denominations considered in this exercise are: Pennies (1¢), Nickels (5¢), Dimes (10¢) and Quarters (25¢). Therefor the dictionary returned should contain exactly 4 key/value pairs.

Notes:

If the function is passed either 0 or a negative number, the function should return the dictionary with all values equal to 0.
If a float is passed into the function, its value should be be rounded down, and the resulting dictionary should never contain fractions of a coin.
Examples
loose_change(56)    ==>  {'Nickels': 1, 'Pennies': 1, 'Dimes': 0, 'Quarters': 2}
loose_change(-435)  ==>  {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
loose_change(4.935) ==>  {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 0}
"""


def loose_change(cents):
    money = {
        'Nickels' : 0,
        'Pennies' : 0,
        'Dimes' : 0,
        'Quarters' :0
    }

    def change(n, m):
      if n < 1 : return m
      if n >= 25:
        new = n-25
        m['Quarters'] +=1
      elif n >= 10:
        new = n-10
        m['Dimes'] +=1
      elif n >= 5:
        new = n-5
        m['Nickels'] +=1
      elif n >= 1:
        new = n-1
        m['Pennies'] +=1
      else : return m
      return change(new, m)

    return change(cents, money)

"""
Other Answers
"""

def loose_change(cents):
    res = {}
    res['Quarters'], cents = divmod(cents, 25) if cents > 0 else (0, 0)
    res['Dimes'], cents = divmod(cents, 10)
    res['Nickels'], cents = divmod(cents, 5)
    res['Pennies'], cents = divmod(cents, 1)
    return res


def loose_change(cents):
    coins = {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    if cents <= 0:
        return coins
    coins['Quarters'] = cents // 25
    coins['Dimes'] = cents % 25 // 10
    coins['Nickels'] = cents % 25 % 10 // 5
    coins['Pennies'] = cents % 25 % 10 % 5 // 1

    return coins
