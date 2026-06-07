from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1 for _ in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False

        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx

        self.parent[ry] = rx
        self.size[rx] += self.size[ry]
        return True


class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        for i, j in hits:
            if grid[i][j] == 1:
                grid[i][j] = 2

        # Virtual node representing the ceiling
        ceiling_idx = rows * cols
        uf = UnionFind(rows * cols + 1)

        def union_neighbor(x, y):
            idx = x * cols + y
            if x == 0:  # directly touches the ceiling
                uf.union(ceiling_idx, idx)
            for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                    neighbor = nx * cols + ny
                    uf.union(idx, neighbor)

        # after all hits have happened
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    union_neighbor(i, j)

        # reverse add the bricks
        ans = [0] * len(hits)
        for i in range(len(hits) - 1, -1, -1):
            r, c = hits[i]
            if grid[r][c] == 2:
                prev_stable = uf.size[uf.find(ceiling_idx)]

                grid[r][c] = 1
                union_neighbor(r, c)

                curr_stable = uf.size[uf.find(ceiling_idx)]
                ans[i] = max(0, curr_stable - prev_stable - 1)
        return ans


grid = [[1, 0, 0, 0],
        [1, 1, 1, 0]]
hits = [[1, 0]]
print(Solution().hitBricks(grid, hits))

grid = [[1, 0, 0, 0],
        [1, 1, 0, 0]]
hits = [[1, 1], [1, 0]]
print(Solution().hitBricks(grid, hits))
