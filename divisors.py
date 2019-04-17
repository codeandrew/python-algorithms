def divisors(n):
    d = 0
    for i in range(n+1):
        if n % (i+1) == 0 : d += 1
    return d


"""
Best Practice
"""
def divisors(n):
    return sum(1 for i in xrange(1, n + 1) if n % i == 0)
