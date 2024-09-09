from collections import deque


class Solution:

    def neighbors(self, r, c, n, m, ht):
        ans = []
        for x, y in [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]:
            if (0 <= x <= n - 1) and (0 <= y <= m - 1):
                # height which is greater from there only
                # water will flow into the ocean
                if ht[x][y] >= ht[r][c]:
                    ans.append((x, y))
        return ans

    def water_flow(self, ht, n, m) -> int:
        atlantic = deque()
        vis_atlantic = set()

        pacific = deque()
        vis_pacific = set()

        for r in range(n):
            for c in range(m):
                if r == 0 or c == 0:
                    atlantic.append((r, c))
                    vis_atlantic.add((r, c))
                if r == n - 1 or c == m - 1:
                    pacific.append((r, c))
                    vis_pacific.add((r, c))

        self.ocean_traversal(atlantic, ht, m, n, vis_atlantic)
        self.ocean_traversal(pacific, ht, m, n, vis_pacific)

        return len(vis_atlantic.intersection(vis_pacific))

    def ocean_traversal(self, ocean, ht, m, n, vis_ocean):
        while ocean:
            x, y = ocean.popleft()
            for (nr, nc) in self.neighbors(x, y, n, m, ht):
                if (nr, nc) not in vis_ocean:
                    vis_ocean.add((nr, nc))
                    ocean.append((nr, nc))


if __name__ == '__main__':
    n = 5
    m = 5
    mat = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4]
    ]
    print(Solution().neighbors(1, 2, 5, 5, mat))
    print(Solution().water_flow(mat, n, m))
