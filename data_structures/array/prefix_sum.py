"""
Notes:
We use prefixes and postfixes to precompute information about subarrays so we can answer range queries or build solutions in O(1) per query instead of O(n).

Prefix
A prefix of an array A is any contiguous subarray A[0…i] for 0 ≤ i < n.

Postfix (Suffix)
A postfix or suffix of an array A is any contiguous subarray A[i…n–1] for 0 ≤ i < n.

Prefix Sum
An array P of length n where
 P[i] = A[0] + A[1] + … + A[i]
Queries: sum of A[l…r] = P[r] – (l > 0 ? P[l–1] : 0)
Build in O(n), answer each range-sum in O(1).

Prefix Product
An array Q of length n where
 Q[i] = A[0] × A[1] × … × A[i]
Queries (when no zeros): prod of A[l…r] = Q[r] ÷ (l > 0 ? Q[l–1] : 1)
Build in O(n), answer each range-product in O(1).

Suffix Sum
Similarly, S[i] = A[i] + A[i+1] + … + A[n–1]
Allows O(1) queries for sums ending at end or to combine with prefix sums.

Suffix Product
Similarly, R[i] = A[i] × A[i+1] × … × A[n–1]

Uses and Examples
• Range‐sum queries (static)
• “Product of array except self” by combining prefix and suffix products
• Fast computation of sliding‐window aggregates when window aligns with ends
• Building DP solutions where state depends on all prior elements (prefix) or all following elements (suffix)
"""

class PrefixSum:
    def __init__(self, nums) -> None:
        self.prefix = []
        total = 0
        for num in nums:
            total += num
            self.prefix.append(total)

    def rangeSum(self, left, right):
        # 1, 4, 3, 6
        # right - (left-1)
        right = self.prefix[right]
        left = self.prefix[left - 1] if left > 0 else 0
        return right - left

