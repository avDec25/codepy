class Solution:
    pits = []

    def neighbors(self, r, c):
        return [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]

    def dfs(self, r, c, ht):
        R = len(ht)
        C = len(ht[0])
        reached_indian = False
        reached_arabian = False

        stack = []
        visited = set()

        stack.append((r, c))
        visited.add((r, c))

        print("==============")
        while stack:
            print(stack)
            pr, pc = stack.pop()
            for nr, nc in self.neighbors(pr, pc):
                if nr == -1 or nc == -1:
                    reached_indian = True
                if nr == R or nc == C:
                    reached_arabian = True

                if (reached_arabian and reached_indian):
                    return True

                if (0 <= nr <= R - 1 and 0 <= nc <= C - 1) \
                        and (ht[pr][pc] >= ht[nr][nc]) \
                        and ((nr, nc) not in visited):
                    if (nr,nc) in self.pits:
                        return True
                    stack.append((nr, nc))
                    visited.add((nr, nc))

        return reached_arabian and reached_indian

    def water_flow(self, mat, n, m) -> int:
        ans = 0
        self.pits = []
        for r in range(n):
            for c in range(m):
                if self.dfs(r, c, mat):
                    self.pits.append((r,c))
                    ans += 1
        return ans


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
    print(Solution().water_flow(mat, n, m))
