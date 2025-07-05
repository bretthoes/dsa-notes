"""
Find the length of the longest subarray, with the same value in each position
"""
def longestSubarray(nums):
    length, L = 0, 0
    for R in range(len(nums)):
        if nums[L] != nums[R]:
            L = R
        length = max(length, R - L + 1)
    return length

print(longestSubarray([4,2,2,3,3,3]))

"""
Find the minimum length subarray, where the sum is greater than or equal to the target.
Assume all values are positive.
"""
def shortestSubarray(nums, target):
    L, total = 0, 0
    length = float("inf")
    for R in range(len(nums)):
        total += nums[R]
        while total >= target:
            length = min(length, R - L + 1)
            total -= nums[L]
            L += 1
    return 0 if length == float("inf") else length


print(shortestSubarray([2,3,1,2,4,3], 6))
