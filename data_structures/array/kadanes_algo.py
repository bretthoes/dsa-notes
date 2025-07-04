# find a non-empty sub-array with the largest sum.
# O(n)
def kadanes(nums):
    maxSum = nums[0]
    curSum = 0

    for n in nums:
        # if current sum goes negative at any point, restart to 0
        curSum = max(curSum, 0)
        curSum += n
        maxSum = max(maxSum, curSum)
    return maxSum

print(kadanes([4, -1, 2, -7, 3, 4]))
# output: 7

# return the left and right index of the max subarray sum.
# assume there's exactly one valid result (no ties).
# O(n)
def sliding_window_kadanes(nums):
    maxSum = nums[0]
    curSum = 0
    maxL, maxR, = 0, 0
    L = 0

    for R in range(len(nums)):
        if curSum < 0:
            curSum = 0
            # window starts at current iterator now
            L = R

        curSum += nums[R]
        if curSum > maxSum:
            maxSum = curSum
            maxL, maxR = L, R

    return [maxL, maxR]

print(sliding_window_kadanes([4, -1, 2, -7, 3, 4]))
# output: [4, 5]


