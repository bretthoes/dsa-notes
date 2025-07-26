from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # type matrix
        # approach:
        # iterate thru matrix, if we hit 0, continue
        # if we hit 1 that isnt visited,
        # dfs to update all adjacent 1s to visited,
        # increment island counter by 1
        def dfs(r, c):
            # handle bounds
            if (
                min(r, c) < 0
                or r >= len(grid)
                or c >= len(grid[0])
                or grid[r][c] == 0
                or (r, c) in visit
            ):
                return
            # add nodes to visited
            visit.add((r, c))
            # queue up adjacent land nodes
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)

        count = 0
        visit = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0 or (r, c) in visit:
                    continue
                # we hit a valid unvisited island
                dfs(r, c)
                count += 1

        return count
