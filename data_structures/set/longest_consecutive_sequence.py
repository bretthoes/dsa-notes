from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # ideas:
        # convert array to set
        # iterate thru nums 
        # if num - 1 isnt it set, we can use this as a starting point
        # build the largest possible sequence from here
        # track current consecutive run and max consecutive run
        nums_set = set(nums) # O(n)

        max_run = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                curr_run = 0
                curr_num = num
                while curr_num in nums_set:
                    curr_num += 1
                    curr_run += 1
                max_run = max(max_run, curr_run)
        return max_run
                
