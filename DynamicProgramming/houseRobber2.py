from functools import lru_cache
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def solve(a):
            m = len(a)
            @lru_cache
            def f(i):
                if i >= m:
                    return 0
                return max(a[i] + f(i+2), f(i+1))
            return f(0)

        # general concept with Circular
        # because we can take either one of the two
        # the last element or the first element in the array
        # we force-exclude one each time
        # take the maximum among the two answers
        return max(
            solve(nums[:-1]),
            solve(nums[1:])
        )

nums = [2,3,2]
print(Solution().rob(nums))

nums = [1,2,3,1]
print(Solution().rob(nums))

nums = [1,2,3]
print(Solution().rob(nums))
