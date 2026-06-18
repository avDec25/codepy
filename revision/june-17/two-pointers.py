from typing import List
from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, x in enumerate(nums):
            complement = target - x
            if complement in seen:
                return [seen[complement] + 1, i + 1]
            seen[x] = i

        return []

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            lo, hi = i + 1, n - 1
            while lo < hi:
                total = nums[i] + nums[lo] + nums[hi]
                if total < 0:
                    lo += 1
                elif total > 0:
                    hi -= 1
                else:
                    ans.append([nums[i], nums[lo], nums[hi]])
                    while lo < hi and nums[lo] == nums[lo + 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi - 1]:
                        hi -= 1
                    lo += 1
                    hi -= 1
        return ans

    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        mx_area = 0

        while left < right:
            width = right - left + 1
            ht = min(height[left], height[right])

            area = width * ht
            mx_area = max(mx_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return mx_area

    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        mx_left, mx_right = 0, 0
        ans = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] > mx_left:
                    mx_left = height[left]
                else:
                    ans += mx_left - height[left]
                left += 1
            else:
                if height[right] > mx_right:
                    mx_right = height[right]
                else:
                    ans += mx_right - height[right]
                right -= 1

        return ans


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(Solution().maxArea(height))

height = [1, 1]
print(Solution().maxArea(height))
