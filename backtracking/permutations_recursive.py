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
    # Recursive helper function that starts inserting elements at index `i`
    def helper(i):
        # Base case: if we've processed all elements, return a list with an empty list (1 permutation of empty list)
        if i == len(nums):
            return [[]]

        resPerms = []  # This will hold all permutations at the current level
        perms = helper(i + 1)  # Recurse to get permutations of the remaining elements

        # For each smaller permutation...
        for p in perms:
            # ...insert nums[i] at every possible position in that permutation
            for j in range(len(p) + 1):
                pCopy = p.copy()  # Make a copy to avoid modifying the original
                pCopy.insert(j, nums[i])  # Insert current element at position j
                resPerms.append(pCopy)  # Add the new permutation to the result list

        return resPerms

    # Start recursion from the 0th index
    return helper(0)

print(permutationsRecursive([1,2,3]))
