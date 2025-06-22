"""
Backtracking:
Count the unique paths from the top left to the bottom right.
A single path can onl move along 0's and shouldn't visit the same cell more than once.
"""
grid = [[0,0,0,0],
        [1,1,0,0],
        [0,0,0,1],
        [0,1,0,0]]

# O(4^n)
def dfs(grid, r, c, visited: set):
    ROWS, COLS = len(grid), len(grid[0])
    if min(r,c) < 0 or r >= ROWS or c >= COLS or (r, c) in visited or grid[r][c] != 0:
        return 0

    if r == ROWS - 1 and c == COLS - 1:
        return 1

    visited.add((r,c))

    count = 0
    count += dfs(grid, r-1, c, visited)
    count += dfs(grid, r+1, c, visited)
    count += dfs(grid, r, c-1, visited)
    count += dfs(grid, r, c+1, visited)

    visited.remove((r,c))

    return count

paths = dfs(grid, 0, 0, set())
print("dfs: ", paths)

