from functools import lru_cache

import sys

sys.setrecursionlimit(5000)


class Solution:
    a = []

    def matrixMultiplication(self, N, a):
        dp = [[0 for _ in range(N)] for _ in range(N)]
        for m in range(2, N): # m = len of matrix
            for i in range(N - m):
                j = i + m
                dp[i][j] = sys.maxsize
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j],
                                   dp[i][k] + dp[k][j] + a[i] * a[k] * a[j])
        return dp[0][N - 1]

    @lru_cache()
    def mcm(self, i, j):
        if i >= j:
            return 0

        ans = sys.maxsize
        for k in range(i, j):
            curr = self.mcm(i, k) + self.mcm(k + 1, j) \
                   + self.a[i - 1] * self.a[k] * self.a[j]
            ans = min(ans, curr)

        return ans

    def matrixMultiplication_v1(self, N, a):
        self.a = a
        return self.mcm(0, N - 1)


N = 5
a = [40, 20, 30, 10, 30]
print(Solution().matrixMultiplication(N, a))
