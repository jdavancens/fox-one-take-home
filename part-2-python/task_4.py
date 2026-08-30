# recursive fibonacci. fine for small n. large n throws RecursionError: maximum recursion depth exceeded
def fib(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)

def fib_iter(n):
    if n <= 0:
        return 0

    a, b = 0, 1

    for _ in range(n):
        a, b = b, a + b
    
    return a

def fib_memo(n, memo=None):
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]
    
    if n <= 0:
        return 0
    
    if n == 1:
        return 1
    
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    
    return memo[n]
    