"""
Sliding Window Fixed

Given an array, return true if there are two elements within a window of size k that are equal.

"""

arr = [1, 2, 3, 2, 3, 3]
k = 2
# true

def has_duplicate_within_window(nums, k):
    """
    Return True if any value appears twice inside any contiguous
    subarray of length k, otherwise False.
    O(n)
    """
    vals = set()
    for R, num in enumerate(nums):
        # if we surpass a valid window length, drop off the value that is no longer in the window
        if R >= k:
            vals.discard(nums[R - k])

        if num in vals:
            return True

        vals.add(num)

    return False

