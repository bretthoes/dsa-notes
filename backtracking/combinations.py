"""
Combinations

Problem - n choose k math problem
Given two nums n & k, return all possible combinations of size=k, choosing from values between 1 and n.

Imagine n=5 and k=2, so all possibilities would be:
[1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]

This can be similar to subsets, again, for every number 1-5 (or 1-n), we have two choices:
    1. Include
    2. Don't include

"""
def combinations(n, k):
    """
    Time: O(k * 2^n)
    """
    combs, curComb = [], []

    def helper(i):
        if len(curComb) == k:
            combs.append(curComb.copy())
            return
        if i > n:
            return

        # decision to include i
        curComb.append(i)
        helper(i + 1)
        curComb.pop()

        # decision to NOT include i
        helper(i + 1)
        
    helper(1)
    return combs


print(combinations(n=5,k=2))

"""
But, there's a more optimal way. If n=5, and we want all combinations of size 2 from 1-5, how many combinations are actually possibly? This is the theoretical limit.
Well, we know we have to create some number (we'll call it x) of combinations, and each will be of size k.
So the best theoretical time complexity is O(x * k)

There's actually a math formula for this.
This is called n choose k, can be written as C(n, k), and the formula would be:
n! / k! * (n - k)!

In our code, this may look like starting at one, then including every possible option from 1-5.
So we would immediately append [1,2],[1,3],[1,4],[1,5].
But, when we do this for the next value, 2, we need to make sure we're not adding a duplicate subset.
So we would skip 1 (or all values already visited) and just append: [2,3],[2,4],[2,5].
And so on!
"""

def combinations_optimal(n, k):
    """
    Time complexity: O(j * C(n,k))
    """
    combs, curComb = [], []
    def helper(i):
        if len(curComb) == k:
            combs.append(curComb.copy())
            return
        if i > n:
            return

        for j in range(i, n + 1):
            curComb.append(j)
            helper(j + 1)
            curComb.pop()
        pass
    helper(1)
    return combs
print(combinations_optimal(5,2))

















