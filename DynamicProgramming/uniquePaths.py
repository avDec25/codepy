import collections


class Solution:
    def neighbours(self, x, y, R, C):
        ans = []
        for nx, ny in [(x + 1, y), (x, y + 1)]:
            if nx < R and ny < C:
                ans.append((nx, ny))
        return ans

    def uniquePaths_v1(self, m: int, n: int) -> int:
        ans = 0
        q = collections.deque()
        q.append((0, 0))

        visited = set()

        while q:
            px, py = q.popleft()
            print(f"(px, py) = ({px}, {py})")
            if (px, py) == (m - 1, n - 1):
                ans += 1
            for nx, ny in self.neighbours(px, py, m, n):
                q.append((nx, ny))

        return ans

    def uniquePaths(self, m: int, n: int) -> int:
        aboveRow = [1 for _ in range(n)]

        for _ in range(m - 1):
            curr_row = [1 for _ in range(n)]
            for i in range(1, n):
                curr_row[i] = curr_row[i - 1] + aboveRow[i]
            aboveRow = curr_row

        return aboveRow[-1]


m = 3
n = 7
print(Solution().uniquePaths(m, n))
