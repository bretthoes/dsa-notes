from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        seq = "123456789"
        ans = []
        for k in range(len(str(low)), len(str(high)) + 1):
            for i in range(0, 9 - k + 1):
                val = int(seq[i:i+k])
                if low <= val <= high:
                    ans.append(val)
        return ans

sln = Solution()
sln.sequentialDigits(1,200)
