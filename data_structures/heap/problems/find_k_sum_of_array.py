from typing import List
import heapq

class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        # Step 1: Calculate the max possible subset sum
        # Convert all numbers to positive for max sum
        total = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                total += nums[i]
            else:
                nums[i] = -nums[i]

        # Step 2: Sort the array for consistent processing
        nums.sort()

        # Step 3: Use a min-heap to find k-1 smallest "subtracted sums"
        # Each heap item is a tuple: (current subset sum, index in nums)
        heap = [(nums[0], 0)]
        subtract_sums = [0]  # includes "subtract 0", i.e., the max itself

        while len(subtract_sums) < k:
            curr_sum, i = heapq.heappop(heap)
            subtract_sums.append(curr_sum)

            # Two options: either include next element or replace current one
            if i + 1 < len(nums):
                # Option 1: add nums[i+1] to the subset
                heapq.heappush(heap, (curr_sum + nums[i+1], i + 1))

                # Option 2: replace nums[i] with nums[i+1] in the subset
                heapq.heappush(heap, (curr_sum - nums[i] + nums[i+1], i + 1))

        # Final result: max total - (k-1)th smallest subtraction
        return total - subtract_sums[-1]

sln = Solution()
res = sln.kSum([2,4,-2], 5)
print(res)
