from typing import List


class Solution:
    # total ways to make the amount, with repeated coins allowed
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]

        dp[0][0] = 1
        for r in range(1, len(coins) + 1):  # coin repr row
            for c in range(amount + 1):  # amount in columns
                dp[r][c] += dp[r - 1][c]
                if c - coins[r - 1] >= 0:
                    dp[r][c] += dp[r][c - coins[r - 1]]

        return dp[len(coins)][amount]

    def cc(self, coins, i, amount):
        if amount == 0: return 1
        if i < 0 or amount < 0: return 0
        return self.cc(coins, i - 1, amount) + self.cc(coins, i,
                                                       amount - coins[i])

    # total ways to make the amount, with repeated coins allowed
    def coinChangeRecursive(self, coins, amount):
        return self.cc(coins, len(coins) - 1, amount)


if __name__ == "__main__":
    # coins = [1, 2, 3]
    # amount = 4

    coins = [2, 5, 3, 6]
    amount = 10

    print(Solution().coinChange(coins, amount))
    print(Solution().coinChangeRecursive(coins, amount))
