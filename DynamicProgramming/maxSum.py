# From an array select elements such that they create the maximum possible sum
# we cannot pick two adjacent elements

# House Robber 1 question leetcode

from typing import List
from functools import lru_cache


class Solution:
    def rob(self, a: List[int]) -> int:
        @lru_cache
        def pick(i: int) -> int:
            if i >= len(a): return 0
            return max(
                a[i] + pick(i + 2),
                pick(i + 1)
            )

        return pick(0)


nums = [2, 7, 9, 3, 1]
print(Solution().rob(nums))
