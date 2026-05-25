from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        ans = float('inf')

        while left <= right:
            mid = (right + left) // 2

            if nums[left] <= nums[right]: # array already sorted
                ans = min(ans, nums[left])
                break

            if nums[left] <= nums[mid]: # left side already sorted, inflex point on right
                ans = min(ans, nums[mid])
                left = mid + 1
            else: # right side already sorted, inflex point on left
                ans = min(ans, nums[mid])
                right = mid - 1

        return ans


nums = [3, 4, 5, 1, 2]
print(Solution().findMin(nums))

nums = [4, 5, 6, 7, 0, 1, 2]
print(Solution().findMin(nums))

nums = [11, 13, 15, 17]
print(Solution().findMin(nums))
