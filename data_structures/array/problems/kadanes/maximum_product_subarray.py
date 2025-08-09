from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int | float:
        result = float('-inf')
        curMax, curMin = 1, 1
        for n in nums:
            tmp = curMin * n
            curMin = min(n, curMax * n, curMin * n)
            curMax = max(n, curMax * n, tmp)
            result = max(result, curMax, curMin)
        return result

