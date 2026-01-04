from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        arr = []
        for x in nums:
            arr.append(abs(x))

        arr.sort()
        return abs(arr[-1]) * abs(arr[-2]) * 100000

nums = [-5, 7, 0]
print(Solution().maxProduct(nums))

nums = [-4, -2, -1, -3]
print(Solution().maxProduct(nums))

nums = [0, 10, 0]
print(Solution().maxProduct(nums))
