from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        area = 0

        while left < right:
            # area will be determined by the shorter height
            if height[left] < height[right]:

                # therefore cannot be used, because shorter height determines area,
                # and here this is bigger so maybe right one is area determiner
                if height[left] >= left_max:
                    left_max = height[left]

                else:
                    area += left_max - height[left]

                left += 1

            else:  # similarly

                if height[right] >= right_max:
                    right_max = height[right]

                else:
                    area += right_max - height[right]

                right -= 1
        return area
