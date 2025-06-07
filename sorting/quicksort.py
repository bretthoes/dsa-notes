"""
Quicksort

Time Complexity:
- Best & Average: O(n log n)
- Worst: O(n^2) [rare, usually avoided with randomized pivot]

Space Complexity:
- O(log n) due to recursive call stack (in-place otherwise)

In place: Yes

Stable: No
"""

def quicksort(arr):
    def sort(low, high):
        if high - low <= 1:
            return  # Base case: 0 or 1 element

        # Pivot is the last element in this subarray
        pivot = arr[high - 1]
        left = low

        # Partition the array into < pivot and >= pivot
        for i in range(low, high - 1):
            if arr[i] < pivot:
                # Swap arr[i] with element at 'left' index
                arr[i], arr[left] = arr[left], arr[i]
                left += 1

        # Place pivot in its final sorted position
        arr[high - 1], arr[left] = arr[left], arr[high - 1]

        # Recursively sort left and right subarrays
        sort(low, left)
        sort(left + 1, high)

    sort(0, len(arr))  # Kick off the sorting process


# Demo: Run if this file is executed directly
if __name__ == "__main__":
    nums = [5, 2, 9, 1, 7, 6, 3]
    print("Before sorting:", nums)
    quicksort(nums)
    print("After sorting: ", nums)
