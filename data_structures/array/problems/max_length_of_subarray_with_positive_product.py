from typing import List

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        """
        ideas:
        variable sliding window
        left and right pointers
        current and max length (current always R - L + 1)
        we're really tracking the largest subarray that satisfies:
            - has an even number of negative values
            - does not have any zeros 
        other thoughts:
        - track max at current window if even # of negatives,
          or up until last negative value
        - reset everything if we hit a zero
        """
        n = len(nums)
        negative_index = -1
        L, max_len, total_negatives = 0, 0, 0
        for R in range(n):
            if nums[R] == 0:
                # reset window
                L = R + 1
                negative_index = -1
                total_negatives = 0
                continue
            if nums[R] < 0:
                # track total negatives in window
                total_negatives += 1
                if negative_index < 0:
                    # track first negative in window
                    negative_index = R
            if total_negatives % 2 == 0:
                max_len = max(max_len, R - L + 1)
            else:
                max_len = max(max_len, R - negative_index)

        return max_len

    
