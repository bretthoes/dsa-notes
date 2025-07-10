"""
Problem:
  Given a list of numbers (with duplicates), return all distinct subsets.
  Example input: [2, 1, 2, 3]

Steps:

1. Sort the array: O(n log n).  
   Sorted: [1, 2, 2, 3]  
   Why? Duplicates become adjacent, so we can skip over them and avoid generating the same subset more than once.

2. Backtracking framework “binary choice at each index” breaks when there are duplicates:
   - For value “2” appearing twice, naive choices would treat each “2” separately and produce duplicate subsets.

3. Instead, at each run of duplicates, treat the block as two high-level options:
   a) Include none of these duplicates  
   b) Include at least one of these duplicates

   Then, for (b), make a second binary choice on how many to include:
     i) exactly one  
    ii) two or more  
   (With only two duplicates you stop after “two.”)

Decision Tree (include?/skip? blocks of duplicates):

Start with sorted list [1, 2, 2, 3]

                [ ]                    ← subset so far
               /   \
        include 1?   (skip 1)
         /      |       \
      Yes        No      sub=[]

If Yes (sub=[1]):  
                [1]  
               /   \
        include 2-block?   (skip 2-block)

     ── No → sub=[1]                  
             ├─ include 3?        → leaves: [1], [1,3]

     ── Yes → decide how many 2’s:
             /        \
       include one?   include both?
       /       |           \
 sub=[1,2]   sub=[1,2,2]    (after either)
  |             |
  ├─ include 3? ├─ include 3?
  |     |       |     |
 [1,2] [1,2,3] [1,2,2] [1,2,2,3]

If No to the 1-branch (sub=[]):
                [ ]
               /   \
        include 2-block?   (skip 2-block)

     ── No → sub=[]
             ├─ include 3?      → leaves: [], [3]

     ── Yes → decide how many 2’s:
             /        \
       include one?   include both?
       /       |           \
  sub=[2]    sub=[2,2]      (after either)
    |           |
  ├─ include 3? ├─ include 3?
  |     |       |     |
 [2]   [2,3]  [2,2] [2,2,3]


Another example:
Subsets of [1, 1, 1, 2] (sorted as [1, 1, 1, 2]):

Start: []

At the run of three 1’s, you have four branches (take 0, 1, 2, or 3 copies):

1) Take 0 of the 1’s → subset so far: []
   ├─ Then at 2:
   │    ├─ Take 0 of the 2’s → []                    (leaf)
   │    └─ Take 1 of the 2’s → [2]                   (leaf)

2) Take 1 of the 1’s → subset so far: [1]
   ├─ Then at 2:
   │    ├─ Take 0 of the 2’s → [1]                   (leaf)
   │    └─ Take 1 of the 2’s → [1, 2]                (leaf)

3) Take 2 of the 1’s → subset so far: [1, 1]
   ├─ Then at 2:
   │    ├─ Take 0 of the 2’s → [1, 1]                (leaf)
   │    └─ Take 1 of the 2’s → [1, 1, 2]             (leaf)

4) Take 3 of the 1’s → subset so far: [1, 1, 1]
   ├─ Then at 2:
   │    ├─ Take 0 of the 2’s → [1, 1, 1]             (leaf)
   │    └─ Take 1 of the 2’s → [1, 1, 1, 2]          (leaf)
"""

def subsetWithDuplicates(nums):
    nums.sort()            # [1,1,1,2]
    subsets, curSet = [], []

    def helper(i):
        if i >= len(nums):
            subsets.append(curSet.copy())
            return

        # --- INCLUDE nums[i] branch ---
        curSet.append(nums[i])   # include this copy
        helper(i + 1)            # recurse to decide about the next spot
        curSet.pop()             # back out

        # --- EXCLUDE nums[i] branch ---
        # skip _all_ duplicates of nums[i], so we don't
        # end up generating the same “exclude” path multiple times
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1               # jump past every copy of this value
        helper(i + 1)            # recurse after the last duplicate

    helper(0)
    return subsets

print(subsetWithDuplicates([1,1,1,2]))
















