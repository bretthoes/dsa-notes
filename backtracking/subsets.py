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

