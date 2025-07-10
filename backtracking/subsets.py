"""
Subsets

Combinatorics, math-theory

given a list of distinct nums, return all possible distinct subsets.
[1,2,3] -> [],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]
Notice we end with 8 distinct subsets, or 2^3 where 3 is the length of the set.
2 * 2 * 2 ... = 2^n

This is a decision tree problem, for every index, we have the option to include it, or not to include it.
So given the above example, our decision tree would look like:
Start
 ├─ include 1?
 │   ├─ Yes → subset so far: [1]
 │   │    ├─ include 2?
 │   │    │    ├─ Yes → [1, 2]
 │   │    │    │    ├─ include 3?
 │   │    │    │    │    ├─ Yes → [1, 2, 3]
 │   │    │    │    └─ No  → [1, 2]
 │   │    │    └─ No  → [1]
 │   │    │         ├─ include 3?
 │   │    │         │    ├─ Yes → [1, 3]
 │   │    │         │    └─ No  → [1]
 │   │
 │   └─ No  → subset so far: []
 │        ├─ include 2?
 │        │    ├─ Yes → [2]
 │        │    │    ├─ include 3?
 │        │    │    │    ├─ Yes → [2, 3]
 │        │    │    └─ No  → [2]
 │        │    └─ No  → []
 │        │         ├─ include 3?
 │        │         │    ├─ Yes → [3]
 │        │         └─ No  → []

Remember we also have to iterate through to make each decision,
so we get time complexity: O(n * 2^n)
Space complexity: O(n) -> (height of the tree) 
"""

def subsetsWithoutDuplicates(nums):
    def helper(i):
        if i >= len(nums):
            subsets.append(curSet.copy())
            return
        # decision to include nums[i]
        curSet.append(nums[i])
        helper(i+1)
        curSet.pop()
        #decision to NOT include nums[i]
        helper(i+1)
    subsets, curSet = [], []
    helper(0)
    return subsets

print(subsetsWithoutDuplicates([1,2,3]))

"""
given a list of nums that are not necessarily distinct, return all distinct subsets
[2,1,2,3]

first thing we want to do with this kind of backtracking problem is to sort the array.
sorting an array is generally o(n log n), which isn't such a big deal for backtracking
where the solution is commonly o(2^n) or worse.
why sort?
this lets us build our subsets easier. why? because all duplicates are now adjacent.
but still, why?
imagine the array below, now sorted:
[1,2,2,3]
and we take our same approach as before, each index we have the choice to include, or
to not include. well, when we have multiple values, we have one path that takes one
occurrence of 2, another that takes both occurrences of 2, and another that takes
zero occurrences of 2.
logically, this approach lets us avoid duplicate subsets.

but, how do we do this with our binary approach at each index?
when we encounter duplicates, we still actually have two choices:
    1. include none of the duplicate elements
    2. include one or more of the duplicate elements
then, in our 2nd choice, we can break that down into another binary choice, i.e.
include exactly one, or include two or more.


"""





