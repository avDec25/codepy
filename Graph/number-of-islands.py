from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        r = len(grid)
        c = len(grid[0])

        def dfs(x, y):
            visited.add((x, y))

            for nx, ny in [
                (x, y+1), (x, y-1), (x-1, y), (x+1, y)
            ]:
                if (
                    0 <= nx < r
                    and 0 <= ny < c
                    and (nx, ny) not in visited
                    and grid[nx][ny] == '1'
                ):
                    dfs(nx, ny)

        visited = set()
        for x in range(r):
            for y in range(c):
                if (x, y) not in visited and grid[x][y] == '1':
                    islands += 1
                    dfs(x, y)

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
