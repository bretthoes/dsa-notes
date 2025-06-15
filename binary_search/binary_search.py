"""
Binary Search

Time Complexity:
Average/Worst Case -> O(log n)
Best Case -> O(1)

Space Complexity:
O(1)
"""
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            return mid
    return -1

arr = [1,4,6,8,9,12,55,89]
target = 8
i = binary_search(arr,target)
print(i)
