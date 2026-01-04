# 4Sum - Find all unique quadruplets that sum to a target value.
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left, right = j + 1, n - 1
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s < target:
                        left += 1
                    elif s > target:
                        right -= 1
                    else:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

        return ans


nums = [1, 0, -1, 0, -2, 2]
target = 0
print(Solution().fourSum(nums, target))
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

nums = [2, 2, 2, 2, 2]
target = 8
print(Solution().fourSum(nums, target))
# Output: [[2,2,2,2]]
