from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return -1


nums = [2, 5]
target = 5
print(Solution().search(nums, target))

nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(Solution().search(nums, target))

nums = [-1, 0, 3, 5, 9, 12]
target = 2
print(Solution().search(nums, target))
