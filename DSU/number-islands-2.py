class Solution:
    def numIslands2(self, rows, cols, positions):
        parent = {}
        size = {}
        ans = []
        islands = 0
        land = set()

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False

            if size[rx] < size[ry]:
                rx, ry = ry, rx

            parent[ry] = rx
            size[rx] += size[ry]

            return True

        for r, c in positions:
            if (r, c) in land:
                ans.append(islands)
                continue

            land.add((r,c))
            islands += 1
            current = r * cols + c
            parent[current] = current
            size[current] = 1

            for nx, ny in [
                (r + 1, c),
                (r - 1, c),
                (r, c + 1),
                (r, c - 1),
            ]:
                if (nx, ny) in land:
                    neighbor = nx * cols + ny
                    if union(current, neighbor):
                        islands -= 1

            ans.append(islands)

        return ans


m = 3
n = 3
positions = [[0, 0], [0, 1], [1, 2], [2, 1]]
print(Solution().numIslands2(m, n, positions))

m = 3
n = 3
positions = [[0, 0], [0, 1], [1, 2], [2, 1], [1, 1]]
print(Solution().numIslands2(m, n, positions))
