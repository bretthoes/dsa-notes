class Solution:
    def numberOfWays(self, s: str) -> int:
        # get total counts
        total_0 = 0
        total_1 = 0
        for char in s:
            if char == '0':
                total_0 += 1
            else:
                total_1 += 1
        
        left_0, left_1 = 0, 0
        count = 0
        for char in s:
            if char == '0':
                right_1 = total_1 - left_1
                count += left_1 * right_1
                left_0 += 1
            if char == '1':
                right_0 = total_0 - left_0
                count += left_0 * right_0
                left_1 += 1
        return count
        
