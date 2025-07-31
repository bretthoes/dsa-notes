from typing import List

class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        # ideas:
        # prefix sum?
        # create new bool array, iterate thru backwards, update bool array i if security[i]: 
        # - has k decreasing values (going backwards)
        # - at least k days before n
        n = len(security)
        k = time
        decreasing = [False] * n
        decreasing_run = 0
        for i in range(n-1, -1, -1):
            if i < n-1 and security[i] <= security[i+1]:
                decreasing_run += 1
            else:
                decreasing_run = 0
            decreasing[i] = decreasing_run >= k and n - i + 1 >= k
        # then iterate thru forwards, track increasing_run similar to above, as well
        # as k days after i, if all conditions true, append to a good_days arr
        good_days = []
        decreasing_run = 0
        for i in range(n):
            if i > 0 and security[i] <= security[i-1]:
                decreasing_run += 1
            else:
                decreasing_run = 0
            if decreasing[i] and decreasing_run >= k and i >= k:
                good_days.append(i)
        return good_days

