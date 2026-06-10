from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, x in enumerate(nums):
            complement = target - x
            if complement in seen:
                return [complement[x] + 1, i + 1]
            seen[x] = i
        return []

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break

            lo = i + 1
            hi = len(nums) - 1
            while lo < hi:
                total = nums[i] + nums[lo] + nums[hi]
                if total == 0:
                    ans.append([nums[i], nums[lo], nums[hi]])

                    while lo < hi and nums[lo] == nums[lo + 1]:
                        lo += 1

                    while lo < hi and nums[hi] == nums[hi - 1]:
                        hi -= 1
                elif total < 0:
                    lo += 1
                else:
                    hi -= 1

        return ans

    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        mx_area = 0
        while left < right:
            ht = min(height[left], height[right])
            width = right - left

            area = ht * width
            mx_area = max(area, mx_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return mx_area

    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        mx_left = 0
        mx_right = 0
        water = 0
        while left < right:
            if height[left] < height[right]:
                if mx_left < height[left]:
                    mx_left = height[left]
                else:
                    water += mx_left - height[left]
                left += 1
            else:
                if mx_right < height[right]:
                    mx_right = height[right]
                else:
                    water += mx_right - height[right]
                right -= 1
        return water
