from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # problem type:
        # sliding window
        q = deque() # deque stores only indexes in k
        result = []
        for i in range(len(nums)):
            # handle removing elements from left
            while q and q[0] <= i - k:
                q.popleft()
            # add new element to window; left if largest
            if not q or nums[i] > nums[q[0]]:
                q.appendleft(i)
            else:# pop from right until not larger than rightmost
                while q and nums[i] > nums[q[-1]]:
                    q.pop()
                q.append(i)
            # record local max if in a valid window
            if i + 1 >= k:
                result.append(nums[q[0]])

        return result
