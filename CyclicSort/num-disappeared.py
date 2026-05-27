from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] *= -1
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]


nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(Solution().findDisappearedNumbers(nums))

nums = [1, 1]
print(Solution().findDisappearedNumbers(nums))
