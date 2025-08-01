from typing import List

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        # iterate thru travel
        # build a prefix sum for travel to each index
        # iterate thru garbage
        # track where we saw the last G, P, and M
        # also track total chars in garbage array
        # answer is total chars + prefix[G] + prefix[P] + prefix[M]
        
        prefix = [0] * len(travel)
        prefix[0] = travel[0]
        for i in range(1, len(travel)):
            prefix[i] += travel[i] + prefix[i-1]

        # -1 indicates none of this garbage type in array
        G, P, M = -1, -1, -1
        total_garbage = 0
        for i, stop in enumerate(garbage):
            for item in stop:
                if item == "G":
                    G = i
                elif item == "P":
                    P = i
                elif item == "M":
                    M = i
                total_garbage += 1
        
        result = total_garbage
        if G > 0:
            result += prefix[G - 1]
        if P > 0:
            result += prefix[P - 1]
        if M > 0:
            result += prefix[M - 1]
        
        return result
                

        
