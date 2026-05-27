from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        r = len(grid)
        c = len(grid[0])
        rotten = deque([])

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        minutes_passed = 0
        while rotten and fresh > 0:
            minutes_passed += 1
            for _ in range(len(rotten)):
                x, y = rotten.popleft()
                for nx, ny in [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]:
                    if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        rotten.append((nx, ny))
                        fresh -= 1

        return minutes_passed if fresh == 0 else -1


grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
print(Solution().orangesRotting(grid))

grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
print(Solution().orangesRotting(grid))

grid = [[0, 2]]
print(Solution().orangesRotting(grid))
