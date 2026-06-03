from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = {}
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in mp:
                return [mp[complement] + 1, i + 1]
            else:
                mp[num] = i
        return None

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        i = 0
        ans = []
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            if nums[i] > 0:
                break

            lo, hi = i+1, n-1
            while lo < hi:
                total = nums[i] + nums[lo] + nums[hi]
                if total == 0:
                    ans.append([nums[i], nums[lo], nums[hi]])
                    while lo < hi and nums[lo] == nums[lo+1]:
                        lo += 1
                    while hi and nums[hi] == nums[hi-1]:
                        hi -= 1
                    lo += 1
                    hi -= 1
                elif total < 0:
                    lo += 1
                else:
                    hi -= 1
        
        return ans


    def maxArea(self, height: List[int]) -> int:
        mx_area = 0
        n = len(height)
        left, right = 0, n - 1

        while left < right:
            mx_area = max(mx_area, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return mx_area

    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        water = 0
        left_mx, right_mx = 0, 0
        
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_mx:
                    left_mx = height[left]
                else:
                    water += left_mx - height[left]
                left += 1
            else:
                if height[right] >= right_mx:
                    right_mx = height[right]
                else:
                    water += right_mx - height[right]
                right -= 1

        return water