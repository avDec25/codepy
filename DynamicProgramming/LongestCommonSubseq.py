from functools import lru_cache


class Solution:
    def longestCommonSubsequence(self, a: str, b: str) -> int:
        self.a = a
        self.b = b
        # memoization
        print(self.lcs(len(a) - 1, len(b) - 1))

        n = len(a)+1
        m = len(b)+1

        dp = [[0 for _ in range(m)] for _ in range(n)]
        print(f"dp({len(dp)} x {len(dp[0])})")

        for i in range(1, n):
            for j in range(1, m):
                if a[i-1] == b[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[n - 1][m - 1]

    @lru_cache
    def lcs(self, i, j):
        # print(f"lcs({i}, {j})")
        if i < 0 or j < 0:
            return 0

        if self.a[i] == self.b[j]:
            return 1 + self.lcs(i - 1, j - 1)

        return max(self.lcs(i - 1, j), self.lcs(i, j - 1))


L = "bsbininm"
M = "jmjkbkjkv"
# print(Solution().lcs(len(L), len(M)))
print(Solution().longestCommonSubsequence(L, M))
