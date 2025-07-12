"""
Permutations

Given a list of nums, return all possible distinct permutations of nums.
[1,2,3,4] 
Total permutations = n! where n is len(nums)

There are several approaches:
    1. Backtracking
    2. Iterative

For each layer, we could choose every other option than what's been included in the tree.
if we have 1,2,3,4 at the top layer, we could do:

    1 -> 2 -> 3
           -> 4
      -> 3 -> 2
           -> 4
      -> 4 -> 2
           -> 3
Then we do this for each value, to get every permutation.
This works, but is a little clunky, because we'll need to manually remove duplicates.

Another similar option, is to start the at beginning, and for every folowing number, insert it either before or after.
So starting with 1, the options would be:
    1 -> [1, 2]
      -> [2, 1]
      -> [1, 3]
      -> [3, 1]
      ...
"""
def permutationsRecursive(nums):
    def helper(i):
        if i == len(nums):
            return[[]]
        resPerms = []
        perms = helper(i + 1)
        for p in perms:
            for j in range(len(p) + 1):
                pCopy = p.copy()
                pCopy.insert(j, nums[i])
                resPerms.append(pCopy)
        return resPerms
    return helper(0)

print(permutationsRecursive([1,2,3]))
