# 2-Dimensional Dynamic Programming
# Counting Paths
# Q: Count the number of unique paths from top-left to bottom right, only moving DOWN or to the RIGHT.
grid = [[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]

def bruteForce(grid):
    rows, cols = len(grid), len(grid[0])
    def _bruteForce(r, c):
        if r == rows or c == cols:
            return 0
        if r == rows - 1 and c == cols - 1:
            return 1
        return _bruteForce(r + 1, c) + _bruteForce(r, c + 1) 

    return _bruteForce(0, 0)

print(bruteForce(grid))

# Top down approach
# Think of it like this: At any point in the grid, we can add the total paths to reach the end of the cells below and to the right to get our answer.
# So we solve this problem for every cell in the grid to get the answer for the 1st (top left) cell.
def memoization(grid):
    rows, cols = len(grid), len(grid[0])
    def _memo(r, c, cache):
        if r == rows or c == cols:
            return 0
        if r == rows - 1 and c == cols - 1:
            return 1
        if cache[r][c] > 0:
            return cache[r][c]

        cache[r][c] = _memo(r + 1, c, cache) + _memo(r, c + 1, cache)
        return cache[r][c]

    return _memo(0, 0, [[0] * len(grid) for _ in range(len(grid[0]))])

print (memoization(grid))
