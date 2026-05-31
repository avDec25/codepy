from collections import defaultdict
from functools import lru_cache


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = defaultdict()
        def func(x):
            if x < 0:
                return 0
            if x == 0:
                return 1

            if x in memo:
                return memo[x]

            memo[x] = func(x - 1) + func(x - 2)
            return memo[x]

        return func(n)


n = 2
print(Solution().climbStairs(n))

n = 3
print(Solution().climbStairs(n))
