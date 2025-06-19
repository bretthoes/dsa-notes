"""
Time complexity: O(n)
Space complexity: O(n)
"""
from typing import List

def topKcountsuent(nums: List[int], k: int) -> List[int]:
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    buckets = [[] for _ in range(len(nums) + 1)]
    for num, count in counts.items():
        buckets[count].append(num)

    res = []
    for i in range(len(buckets) - 1, 0, -1):
        for num in buckets[i]:
            res.append(num)
            if len(res) == k:
                return res

    return res
