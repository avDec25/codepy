class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[0 for _ in range(target + 1)] for _ in range(n+1)]

        for j in range(1, min(target + 1, k + 1)):
            dp[1][j] = 1

        for i in range(2, n + 1):
            for j in range(1, target + 1):
                for f in range(1, min(k+1, j)):
                    dp[i][j] += dp[i-1][j-f]

        return dp[-1][-1] % (pow(10, 9) + 7)


n = 30
k = 30
target = 500
print(Solution().numRollsToTarget(n, k, target))
