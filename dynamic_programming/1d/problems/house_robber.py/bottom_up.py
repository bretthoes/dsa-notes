from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        problem type:
        1-d dp

        approach:
        since dp, we should break into sub-problems.
        - either we take the value at i, then we need find the largest value from subarray i+2:n
        - or we don't take the value at i, and need to find the largest value from subarray i+1:n

        recurrence relationship:
        from these sub-problems, we build our dp formula, or recurrence relationship:
        rob = max(arr[i] + rob(arr[i+2:n]), rob(arr[i+1:n]))
        """
        dp1, dp2 = 0, 0
        for n in nums:
            tmp = max(dp1 + n, dp2)
            dp1 = dp2
            dp2 = tmp
        return dp2
