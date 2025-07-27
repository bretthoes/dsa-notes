from collections import defaultdict
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        # data structures/algos ->
        #   heap
        #   map

        # approach ->
        #   build a map of counts
        #   push all values with count into a max heap
        #   pop two distinct vals at a time off max heap
        #   append these to string, push back to queue if
        #   there count is still > 0
        counts = defaultdict(int)
        for char in s:
            counts[char] += 1
        
        heap = []
        for char, count in counts.items():
            heap.append((-count, char)) # negative to simulate max heap
        heapq.heapify(heap)

        result = []
        while len(heap) >= 2:
            count1, char1 = heapq.heappop(heap)
            count2, char2 = heapq.heappop(heap)

            # Append both characters
            result.append(char1)
            result.append(char2)

            # Decrease counts and reinsert if still available
            if count1 + 1 < 0:
                heapq.heappush(heap, (count1 + 1, char1))
            if count2 + 1 < 0:
                heapq.heappush(heap, (count2 + 1, char2))

        # One character left to place
        if heap:
            count, char = heapq.heappop(heap)
            if -count > 1:
                return ""  # Can't place without repeating
            result.append(char)
            
        return "".join(result)

