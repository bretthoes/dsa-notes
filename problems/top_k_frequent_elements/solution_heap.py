"""
Min-Heap approach: keep a size-k min-heap of (freq, num).
Time: O(n log k) worst-case, Space: O(m + k) extra (map + heap).
"""
from typing import List
import heapq

def topKFrequent(nums: List[int], k: int) -> List[int]:
    # 1. Build frequency map
    counts: dict[int, int] = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    # 2. Maintain a min-heap of size <= k: (freq, num)
    heap: list[tuple[int, int]] = []
    for num, freq in counts.items():
        heapq.heappush(heap, (freq, num))
        # If we exceed k items, pop the smallest freq to keep only top-k
        if len(heap) > k:
            heapq.heappop(heap)

    # 3. Extract from heap into result list
    res: List[int] = []
    # If order doesn’t matter, just pop all:
    while heap:
        res.append(heapq.heappop(heap)[1])
    # Now res has the top-k elements in ascending-frequency order
    # If you want “most frequent first,” reverse:
    res.reverse()
    return res

