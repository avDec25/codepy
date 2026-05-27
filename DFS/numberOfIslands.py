from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r = len(grid)
        c = len(grid[0])

        # explore via dfs
        def dfs_no_recursion(i, j):
            grid[i][j] = "0"
            stk = [(i, j)]

            while stk:
                x, y = stk.pop()
                for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] == "1":
                        grid[nx][ny] = "0"
                        stk.append((nx, ny))

        # explore via dfs
        def dfs(x, y):
            grid[x][y] = "0"
            for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] == "1":
                    dfs(nx, ny)

        def bfs(i, j):
            q = deque([(i, j)])
            while q:
                x, y = q.popleft()
                for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] == "1":
                        q.append((nx, ny))
                        grid[nx][ny] = "0"

        islands = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    islands += 1
                    # bfs(i, j)
                    # dfs(i, j)
                    dfs_no_recursion(i, j)

        return islands


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
print(Solution().numIslands(grid))

grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(Solution().numIslands(grid))
