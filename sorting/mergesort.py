"""
Mergesort

Time Complexity:
 - Best: O(n log n)
 - Average: O(n log n)
 - Worst: O(n log n)

Space Complexity:
 - O(n) for temporary arrays

In Place: ❌ (not in-place, due to extra space)
Stable: ✅ (preserves order of equal elements)
"""
def mergesort(arr):
    def sort(left, right):
        if left >= right:
            return # Base case: 1 or 0 elements

        mid = (left + right) // 2
        sort(left, mid)
        sort(mid+1, right)
        merge(left, mid, right)

    def merge(left, mid, right):
        a1 = arr[left:mid+1]

        a2 = arr[mid+1:right+1]
        
        c1 = 0
        c2 = 0
        arrCounter = left
        while c1 < len(a1) and c2 < len(a2):
            if a1[c1] < a2[c2]:
                arr[arrCounter] = a1[c1]
                arrCounter += 1
                c1 += 1
            else:
                arr[arrCounter] = a2[c2]
                arrCounter += 1
                c2 += 1

        while c1 < len(a1):
            arr[arrCounter] = a1[c1]
            arrCounter += 1
            c1 += 1

        while c2 < len(a2):
            arr[arrCounter] = a2[c2]
            arrCounter += 1
            c2 += 1

    sort(0, len(arr) - 1)

# Demo: Run if this file is executed directly
if __name__ == "__main__":
    nums = [5, 2, 9, 1, 7, 6, 3]
    print("Before sorting:", nums)
    mergesort(nums)
    print("After sorting: ", nums)
