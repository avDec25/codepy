from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1 for _ in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # Union by Size
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False

        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        self.size[rx] += self.size[ry]
        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def component_size(self, x):
        return self.size[self.find(x)]


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        uf = UnionFind((rows*cols) + 1)

        for r in range(rows):
            for c in range(cols):
                id = r * cols + c
                if grid[r][c] == "1":
                    # because elements will be neighbors if top and left are also 1
                    # we are moving front and down, so no need to check them
                    if r > 0 and grid[r - 1][c] == "1":
                        uf.union(id, (r - 1) * cols + c)
                    if c > 0 and grid[r][c - 1] == "1":
                        uf.union(id, r * cols + c - 1)

        islands = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands.add(uf.find(r*cols+c))

        return len(islands)



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
