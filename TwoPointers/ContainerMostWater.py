from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        mx_area = 0

        while left < right:
            width = right - left
            h = min(height[left], height[right])

            area = width * h
            if area > mx_area:
                mx_area = area

            # move away from shorter height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return mx_area

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(Solution().maxArea(height))

height = [1, 1]
print(Solution().maxArea(height))
