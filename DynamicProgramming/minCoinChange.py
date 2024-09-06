from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[float('inf') for i in range(amount + 1)] for _ in
              range(len(coins) + 1)]

        for c in range(amount + 1):
            if c % coins[0] == 0:
                dp[1][c] = c // coins[0]

        for r in range(2, len(coins) + 1):
            for c in range(amount + 1):
                if c == 0:
                    dp[r][0] = 0
                    continue
                dp[r][c] = dp[r - 1][c]
                if c - coins[r - 1] >= 0:
                    dp[r][c] = min(dp[r][c], 1 + dp[r][c - coins[r - 1]])

        # for e in range(len(coins) + 1):
        #     print(dp[e])

        if dp[len(coins)][amount] == float('inf'):
            return -1
        else:
            return dp[len(coins)][amount]


if __name__ == '__main__':
    coins = [2, 5, 10, 1]
    amount = 27
    print(Solution().coinChange(coins, amount))
