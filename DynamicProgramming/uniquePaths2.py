import collections
from typing import List


class Solution:
    def neighbours(self, x, y, R, C, grid):
        ans = []
        for nx, ny in [(x + 1, y), (x, y + 1)]:
            if nx < R and ny < C and grid[nx][ny] == 0:
                ans.append((nx, ny))
        return ans

    def uniquePathsWithObstacles_v1(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if m == 1 and n == 1 and obstacleGrid[0][0] == 1: return 0
        if m == 1 and n == 1 and obstacleGrid[0][0] == 0: return 1

        ans = 0
        q = collections.deque()
        q.append((0, 0))

        while q:
            px, py = q.popleft()
            if (px, py) == (m - 1, n - 1):
                ans += 1
            for nx, ny in self.neighbours(px, py, m, n, obstacleGrid):
                q.append((nx, ny))

        return ans

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if m == 1 and n == 1 and obstacleGrid[0][0] == 1: return 0
        if m == 1 and n == 1 and obstacleGrid[0][0] == 0: return 1

        def path(dp, r, c):
            if r < m and c < n and obstacleGrid[r][c] == 1: return 0
            if r == m-1 and c == n-1: return 1
            if r >= m or c >= n: return 0
            if dp[r][c] != -1: return dp[r][c]
            bottom = path(dp, r+1, c)
            right = path(dp, r, c+1)
            dp[r][c] = bottom + right
            return dp[r][c]

        dp = [[-1 for _ in range(n)] for _ in range(m)]
        path(dp, 0, 0)
        return 0 if dp[0][0] == -1 else dp[0][0]


obstacleGrid = [[0, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 0]]
print(Solution().uniquePathsWithObstacles_v1(obstacleGrid))
print(Solution().uniquePathsWithObstacles(obstacleGrid))
