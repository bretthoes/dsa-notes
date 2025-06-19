"""
Time Complexity:
      - Building the frequency map: O(n), where n = len(nums).
      - Let m = number of unique elements (len(counts)). Sorting the m pairs is O(m log m).
      - Popping k times is O(k).
      Overall worst-case: O(n + m log m). Since m ≤ n, worst-case is O(n log n).
    
    Space Complexity:
      - O(m) extra space for the frequency map.
      - O(m) for the list of [count, num] pairs.
"""

from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    arr = []
    for num, count in counts.items():
        arr.append([count, num])

    arr.sort()

    res = []
    k = min(k, len(arr)) # just in case arr is shorter than k
    for _ in range(k):
        res.append(arr.pop()[1])

    return res

