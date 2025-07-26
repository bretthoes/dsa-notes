from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # problem -> graph, k nearest, adj list?
        # approach -> calculate euclidian distance for all points from origin
        # as we do this, keep a minheap of (negative) values (use a tuple (euclidian_dist, x, y) ) of size k
        # convert heap to list and return
        heap = []
        for x,y in points:
            dist = x * x + y * y
            heapq.heappush(heap, (dist,x,y))

        result = []
        while len(result) < k:
            dist, x, y = heapq.heappop(heap)
            result.append([x,y])
        return result


        
