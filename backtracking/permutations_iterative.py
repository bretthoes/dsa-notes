"""
Generates all permutations of a list of numbers using an iterative approach.

Concept:
- Start with a list containing a single empty permutation: `[[]]`
- For each number in the input list:
    - Insert it into every possible position of every existing permutation
    - This generates a new set of permutations with the current number included
- Repeat until all numbers have been processed

Example:
    Input: [1, 2, 3]
    Step 1: [[]]
    Step 2: [[1]]
    Step 3: [[2,1], [1,2]]
    Step 4: [[3,2,1], [2,3,1], [2,1,3], [3,1,2], [1,3,2], [1,2,3]]

Time complexity:
- O(n^2 * n!) because:
    - There are n! total permutations
    - Inserting a number into a list of size n takes O(n) time
"""
def permutations_iterative(nums):
    perms = [[]]  # Start with one empty permutation

    # Process each number in the input list
    for n in nums:
        nextPerms = []  # Temporary list to hold permutations including `n`

        # For each existing permutation...
        for p in perms:
            # ...insert `n` into every possible position
            for i in range(len(p) + 1):
                pCopy = p.copy()         # Copy to avoid mutating the original list
                pCopy.insert(i, n)       # Insert current number at position i
                nextPerms.append(pCopy)  # Add the new permutation to the list

        perms = nextPerms  # Move to the next level of permutations

    return perms  # Return the final list of all permutations
