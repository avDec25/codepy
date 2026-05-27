from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        while i < n:
            correct = nums[i] - 1
            if 1 <= nums[i] <= n and nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1
            print(nums)

        for i in range(n):
            if 1 + i != nums[i]:
                return i + 1

        return n + 1


nums = [1, 2, 0]
print(Solution().firstMissingPositive(nums))

nums = [3, 4, -1, 1]
print(Solution().firstMissingPositive(nums))

nums = [7, 8, 9, 11, 12]
print(Solution().firstMissingPositive(nums))
