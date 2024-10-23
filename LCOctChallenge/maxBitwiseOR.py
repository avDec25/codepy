import itertools
from typing import List
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        mx_or = 0
        count = 0
        for e in nums:
            mx_or |= e
        for i in range(len(nums)+1):
            for x in itertools.combinations(nums, i):
                x_or = 0
                for e in list(x):
                    x_or |= e
                if x_or == mx_or:
                    count += 1

        return count


nums = [3,1]
print(Solution().countMaxOrSubsets(nums))

nums = [2,2,2]
print(Solution().countMaxOrSubsets(nums))

nums = [3,2,1,5]
print(Solution().countMaxOrSubsets(nums))

