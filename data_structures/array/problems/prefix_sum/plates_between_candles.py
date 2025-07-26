from typing import List

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]):
        # problem -> array, prefix sum

        # approach -> build prefix sum of how many plates are included at each index
        # track position of previous and next candle for each index, build arrays for this as well
        # iterate thru queries, calculate candles between plates using prefix sum and prev/next candle
        prefix = [0] * len(s)
        prev_candle = [-1] * len(s)
        plates = 0
        prev_candle_index = -1
        for i, char in enumerate(s):
            if char == '*':
                plates += 1
            if char == '|':
                prev_candle_index = i
            prefix[i] = plates
            prev_candle[i] = prev_candle_index
        
        next_candle = [-1] * len(s)
        next_candle_index = -1
        for i in range(len(s)-1,-1,-1):
            if s[i] == '|':
                next_candle_index = i
            next_candle[i] = next_candle_index
        
        result = []
        for x, y in queries:
            start = next_candle[x]
            end = prev_candle[y]
            if start < 0 or end < 0 or start >= end:
                result.append(0)
                continue
            plates_for_query = prefix[end] - prefix[start]
            result.append(plates_for_query)
        return result
