from collections import deque

grid = [[0,0,0,0],
        [1,1,0,0],
        [0,0,0,1],
        [0,1,0,0]]

# shortest path from top left to bottom right; O(n)
# goes layer by layer processing queue in iterations;
# useful for counting steps in a bfs style question
def bfs(grid):
    ROWS, COLS = len(grid), len(grid[0])
    count = 0
    queue = deque()
    visited = set()
    start = (0, 0)
    queue.append(start)
    visited.add(start)
    while (queue):
        for _ in range(len(queue)):
            r, c = queue.popleft()
            # check for end state (bottom right)
            if r == ROWS - 1 and c == COLS - 1:
                return count
            # queue up neighbors (if valid coords, and not a 1, and not visited)
            neighbors = [[1,0],[-1,0],[0,1],[0,-1]]
            for nr, nc in neighbors:
                if min(r + nr, c + nc) < 0:
                    continue
                if r + nr >= ROWS or c + nc >= COLS:
                    continue
                if (r + nr, c + nc) in visited:
                    continue
                if grid[r + nr][c + nc] != 0:
                    continue
                visited.add((r + nr, c + nc))
                queue.append((r + nr, c + nc))
        count += 1
    return -1

paths = bfs(grid)
print("bfs:", paths)















