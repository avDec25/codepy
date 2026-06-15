from typing import List


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def climb(steps):
            if steps in memo:
                return memo[steps]

            if steps < 0:
                return 0

            if steps == 0:
                return 1

            memo[steps] = climb(steps - 1) + climb(steps - 2)
            return memo[steps]

        return climb(n)

    def coinChange(self, coins: List[int], amount: int) -> int:

        def f(x):
            if x < 0:
                return -1
            if x == 0:
                return 0

            min_req = float("inf")
            for coin in coins:
                temp = f(x - coin)
                if temp != -1:
                    min_req = min(min_req, temp + 1)

            return min_req

        ans = f(amount)
        if ans == float("inf"):
            return -1
        return ans


coins = [1, 2, 5]
amount = 11
print(Solution().coinChange(coins, amount))

coins = [2]
amount = 3
print(Solution().coinChange(coins, amount))

coins = [1]
amount = 0
print(Solution().coinChange(coins, amount))
