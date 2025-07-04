# --------------------------------------------------------
# 1. Brute-Force Recursive (Exponential Time)
# --------------------------------------------------------
def bruteForce(n):
    """
    – If n ≤ 1, it’s just n (base cases F(0)=0, F(1)=1).
    – Otherwise, recursively compute F(n−1) + F(n−2).

    Time Complexity: O(2^n)
      • Each call spawns two more calls (except at the leaves).
      • The recursion tree has ~2^n nodes.
    Space Complexity: O(n)
      • Max recursion depth is n.
    """
    if n <= 1:
        return n
    return bruteForce(n - 1) + bruteForce(n - 2)


# --------------------------------------------------------
# 2. Top-Down DP with Memoization
# --------------------------------------------------------
def memoization(n, cache):
    """
    – Store results of each Fib(k) in `cache` (e.g. a dict).
    – Recurse like bruteForce, but first check cache to avoid recompute.

    Time Complexity: O(n)
      • Each value F(0)…F(n) computed exactly once.
    Space Complexity: O(n)
      • Cache holds n entries + recursion depth up to n.
    """
    if n <= 1:
        return n
    if n in cache:
        return cache[n]

    cache[n] = memoization(n - 1, cache) + memoization(n - 2, cache)
    return cache[n]

# Usage:
# >>> memoization(10, {})
# 55


# --------------------------------------------------------
# 3. Bottom-Up Iterative DP (“True” DP)
# --------------------------------------------------------
def dp(n):
    """
    – Build from the ground up: start with F(0)=0, F(1)=1.
    – Iteratively compute each next Fib into a small rolling array.

    Time Complexity: O(n)
      • Single loop from 2…n.
    Space Complexity: O(1)
      • Only two variables needed at any time.
    """
    if n <= 1:
        return n

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr


