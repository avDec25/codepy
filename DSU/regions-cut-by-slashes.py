from typing import List


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        parent = list(range(4 * n * n))  # each cell has 4 sections

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[rx] = ry

        def get_index(r, c, tri):
            return (r*n + c)*4 + tri

        for r in range(n):
            for c in range(n):
                top = get_index(r, c, 0)
                left = get_index(r, c, 1)
                right = get_index(r, c, 2)
                bottom = get_index(r, c, 3)

                char = grid[r][c]
                if char == ' ':
                    union(top, left)
                    union(top, right)
                    union(top, bottom)
                elif char == '/':
                    union(top, left)
                    union(right, bottom)
                elif char == '\\':
                    union(top, right)
                    union(left, bottom)

                if 0 <= c-1 < n:
                    left_neighbor_right = get_index(r, c-1, 2)
                    union(left, left_neighbor_right)
                if 0 <= r-1 < n:
                    top_neighbor_bottom = get_index(r-1, c, 3)
                    union(top, top_neighbor_bottom)

        regions = set()
        for i in range(n*n*4):
            regions.add(find(i))
        return len(regions)




grid = [" /", "/ "]
print(Solution().regionsBySlashes(grid))

grid = [" /", "  "]
print(Solution().regionsBySlashes(grid))

grid = ["/\\", "\\/"]
print(Solution().regionsBySlashes(grid))
