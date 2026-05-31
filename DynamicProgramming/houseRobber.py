from functools import lru_cache
from typing import List



class Solution2:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        @lru_cache
        def f(i):
            if i >= n:
                return 0
            return max(nums[i] + f(i+2), f(i+1))
        return f(0)

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def f(i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]
            memo[i] = max(nums[i] + f(i+2), f(i+1))
            return memo[i]
        return f(0)


nums = [1, 2, 3, 1]
print(Solution().rob(nums))

nums = [2, 7, 9, 3, 1]
print(Solution().rob(nums))
