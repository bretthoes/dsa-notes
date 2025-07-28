from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # graph
        # bfs because there could be multiple rotting oranges at the start
        # iterate thru, find bad oranges, add these to queue, queue up all adjacent neighbors on each pass,
        # iterate count for each "layer", mark visited, return once there are no more to process
        # logic should handle bounds, previously visited, and fresh/rotten/empty states

        # iterate thru, find bad oranges
        ROWS, COLS = len(grid),len(grid[0])
        rotting_oranges = []
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rotting_oranges.append((r,c))

        visited = set(rotting_oranges)
        q = deque(rotting_oranges)
        minutes = -1
        NEIGHBORS = [(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for neighbor_row, neighbor_col in NEIGHBORS:
                    next_row, next_col = r + neighbor_row, c + neighbor_col
                    if (min(next_row, next_col) < 0 
                        or next_row >= ROWS
                        or next_col >= COLS 
                        or (next_row, next_col) in visited 
                        or grid[next_row][next_col] == 0):
                        continue
                    grid[next_row][next_col] = 2
                    visited.add((next_row, next_col))
                    q.append((next_row, next_col))
            minutes += 1

        # one last pass thru to check if wewe reached everything
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1

        return max(0, minutes)
                
                    
                    



