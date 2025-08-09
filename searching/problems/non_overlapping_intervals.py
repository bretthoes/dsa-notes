from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[-1])
        prev_end = -float('inf')
        count = 0
        for i in intervals:
            if i[0] < prev_end:
                count += 1
            else: # update prev end if we didnt remove the current interval
                prev_end = i[1]
        return count
