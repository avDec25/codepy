from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            area = h * w
            max_area = max(area, max_area)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_area


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(Solution().maxArea(height))

height = [1, 1]
print(Solution().maxArea(height))
