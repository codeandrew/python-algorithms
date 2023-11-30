"""
Write a function that counts how many different ways you can make change for an amount of money, given an array of coin denominations. For example, there are 3 ways to give change for 4 if you have coins with denomination 1 and 2:

1+1+1+1, 1+1+2, 2+2.
The order of coins does not matter:

1+1+2 == 2+1+1
Also, assume that you have an infinite amount of coins.

Your function should take an amount to change and an array of unique denominations for the coins:

  count_change(4, [1,2]) # => 3
  count_change(10, [5,2,3]) # => 4
  count_change(11, [5,7]) # => 0
"""

def count_change(amount, coins):
    ways = [0] * (amount + 1)
    ways[0] = 1  
    for coin in coins:
        for i in range(coin, amount + 1):
            ways[i] += ways[i - coin]

    return ways[amount]

# clever 
def count_change(n, coin_values):
    return sum(count_change(n - v, coin_values[i:]) for i,v in enumerate(coin_values) if v <= n) if n else 1
