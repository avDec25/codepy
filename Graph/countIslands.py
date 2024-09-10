from collections import deque


class Solution:
    def neighbors(self, r, c, R, C, grid):
        ans = []
        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1),
                       (r + 1, c + 1), (r + 1, c - 1), (r - 1, c + 1),
                       (r - 1, c - 1)]:
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1:
                ans.append((nr, nc))
        return ans

    def numIslands(self, a):
        ans = 0
        R = len(a)
        C = len(a[0])

        q = deque()
        visited = set()

        for r in range(R):
            for c in range(C):
                if (r, c) not in visited and a[r][c] == 1:
                    ans += 1
                    q.append((r, c))
                    visited.add((r,c))
                    while q:
                        u, v = q.pop()
                        for nr, nc in self.neighbors(u, v, R, C, a):
                            if (nr, nc) not in visited:
                                visited.add((nr, nc))
                                q.append((nr, nc))
        return ans


if __name__ == '__main__':
    mat = [[1, 1, 0, 0, 0],
           [0, 1, 0, 0, 1],
           [1, 0, 0, 1, 1],
           [0, 0, 0, 0, 0],
           [1, 0, 1, 1, 0]]
    print(Solution().numIslands(mat))
