from typing import List

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        """
        recursion
        Time: O(n^2)
        Space: O(n^2)
        """
        def _reduce(arr):
            # base case
            n = len(arr)
            if n == 1:
                return arr
            reduced = []

            for i in range(n - 1):
                next_value = (arr[i] + arr[i + 1]) % 10
                reduced.append(next_value)
            return _reduce(reduced) # cut off last element
        
        return _reduce(nums)[0]
        
    @staticmethod
    def triangularSumInPlace(nums: List[int]) -> int:
        """
        Time: O(n)
        Space: O(1)
        """
        n = len(nums)
        for level in range(n):
            for i in range(n - level - 1):
                nums[i] = (nums[i] + nums[i + 1]) % 10
        return nums[0]

Solution.triangularSumInPlace([1,2,3,4])

