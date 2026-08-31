def fib(n):
    """Naive recursion. 

    Readability: closest to mathematical definition. Most readable.
    Performance: exponential, recomputes same n many times, RecursionError on
    large n. Worst performance.
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)

def fib_iter(n):
    """Walk the sequence keeping the last two values. 
    
    Readability: somewhat opaque
    Performance: O(n) time, O(1) extra space, no call stack. Best performance.
    """
    if n <= 0:
        return 0

    a, b = 0, 1

    for _ in range(n):
        a, b = b, a + b
    
    return a

def fib_memo(n, memo=None):
    """Memoized recursion.

    Readability: Same recurrence as fib
    Performance: Caching saves repeated calculations (O(n)). Same recursion 
    problem as fib.
    """
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
    