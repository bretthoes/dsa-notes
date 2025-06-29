# 2-Dimensional Dynamic Programming
# Counting Paths: Count the number of unique paths from top-left to bottom-right,
# moving only DOWN or RIGHT at each step.

grid = [[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]

# --------------------------------------------------------
# 1. Brute-Force Recursive (Exponential Time)
# --------------------------------------------------------
def bruteForce(grid):
    rows, cols = len(grid), len(grid[0])
    def _rec(r, c):
        # If we move outside grid boundaries, no valid path
        if r == rows or c == cols:
            return 0
        # If we've reached bottom-right corner, we've found 1 valid path
        if r == rows - 1 and c == cols - 1:
            return 1
        # Otherwise, sum paths by moving DOWN and RIGHT
        return _rec(r + 1, c) + _rec(r, c + 1)

    return _rec(0, 0)

print(bruteForce(grid))  # ➔ 20 for a 4×4 grid


# --------------------------------------------------------
# 2. Top-Down DP with Memoization (O(m·n) Time, O(m·n) Space)
# --------------------------------------------------------
def memoization(grid):
    rows, cols = len(grid), len(grid[0])
    # cache[r][c] will hold number of paths from (r,c) to end
    cache = [[0] * cols for _ in range(rows)]

    def _rec(r, c):
        # Out of bounds → no paths
        if r == rows or c == cols:
            return 0
        # Reached destination → exactly 1 path
        if r == rows - 1 and c == cols - 1:
            return 1
        # Return cached result if available
        if cache[r][c] != 0:
            return cache[r][c]
        # Compute, cache, and return
        cache[r][c] = _rec(r + 1, c) + _rec(r, c + 1)
        return cache[r][c]

    return _rec(0, 0)

print(memoization(grid))  # ➔ 20


# --------------------------------------------------------
# 3. Bottom-Up Iterative DP (“True” DP — O(m·n) Time, O(n) Space)
# --------------------------------------------------------
def dp(grid):
    rows, cols = len(grid), len(grid[0])
    # We only need one “next row” at a time, so use two 1D arrays
    prev_row = [0] * cols

    # Process rows from bottom up
    for _ in range(rows - 1, -1, -1):
        cur_row = [0] * cols
        # Rightmost cell always has exactly 1 path (can only go down)
        cur_row[cols - 1] = 1

        # Fill current row from right to left
        for c in range(cols - 2, -1, -1):
            # Paths = paths from RIGHT cell + paths from DOWN cell
            cur_row[c] = cur_row[c + 1] + prev_row[c]

        # Roll current row to be prev_row for next iteration (upwards)
        prev_row = cur_row

    # Top-left cell holds the total number of unique paths
    return prev_row[0]

print(dp(grid))  # ➔ 20




