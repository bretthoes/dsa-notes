from typing import List

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # ideas:
        # sort nums
        # prefix sum then binary sort?
        n = len(nums)
        
        nums.sort()
        prefix = [nums[0]]
        for i in range(1, n):
            prefix.append(prefix[i-1] + nums[i])

        answers = []
        for q in queries:
            L, R = 0, len(prefix)-1
            while L <= R:
                mid = (L + R) // 2
                if prefix[mid] <= q:
                    L = mid + 1
                elif prefix[mid] > q:
                    R = mid - 1
            answers.append(R + 1)

        return answers
