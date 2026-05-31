from collections import defaultdict
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = defaultdict()
        def f(n):
            if n in memo:
                return memo[n]

            if n < 0:  # coin change not possible
                return -1
            if n == 0:  # coin change possible
                return 0

            min_count = float('inf') # +ve infinity
            for coin in coins:
                res = f(n - coin)
                if res != -1:  # coin change possible
                    min_count = min(min_count, 1 + res)

            memo[n] = min_count if min_count != float('inf') else -1
            return memo[n]

        return f(amount)


coins = [1, 2, 5]
amount = 11
print(Solution().coinChange(coins, amount))

coins = [2]
amount = 3
print(Solution().coinChange(coins, amount))

coins = [1]
amount = 0
print(Solution().coinChange(coins, amount))
