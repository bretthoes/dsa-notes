"""
With 2 pointers, we generally care more about the two values the pointers are pointing to, whereas in sliding window we are tracking some information about the entire window.
"""
def isPalindrome(arr):
    L, R = 0, len(arr) - 1
    while L < R:
        if arr[L] != arr[R]:
            return False
        L += 1
        R -= 1

    return True

"""
Given a sorted input array, return the two indicies of two elements which sum up to the target value.
Assume there's exactly one solution.
"""
def twoSum(arr, target):
    L, R = 0, len(arr) - 1
    while L < R:
        if arr[L] + arr[R] > target:
            R -= 1
        elif arr[L] + arr[R] < target:
            L += 1
        else:
            return [L, R]
print(twoSum([-1,2,3,4,7,9], 7))
