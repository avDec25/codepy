from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            # works because when we divide the array in two
            # then a part of it we will always find sorted

            # and if we continue to divide it, and process the divided part
            # then on the sub-array also the same properties applies,
            # i.e. the subarray is also rotated sorted
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid

            # checks which part is sorted, l---m or m---r
            if nums[left] <= nums[mid]: # if l---m is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            else: # if m---r is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


nums = [5, 6, 7, 8, 9, 1, 2, 3, 4]
target = 3
print(Solution().search(nums, target))

nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(Solution().search(nums, target))

nums = [4, 5, 6, 7, 0, 1, 2]
target = 7
print(Solution().search(nums, target))

nums = [1]
target = 0
print(Solution().search(nums, target))
