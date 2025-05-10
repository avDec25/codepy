from typing import List


class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        area_max = 0
        for i in range(len(h)):
            width = 0
            for j in range(i - 1, -1, -1):
                if h[j] >= h[i]:
                    width += 1

                else:
                    break

            for j in range(i + 1, len(h)):
                if h[j] >= h[i]:
                    width += 1
                else:
                    break

            area_max = max(area_max, (1 + width) * h[i])

        return area_max


heights = [2, 1, 5, 6, 2, 3]
print(Solution().largestRectangleArea(heights))

heights = [2, 4]
print(Solution().largestRectangleArea(heights))

heights = [2, 0, 2]
print(Solution().largestRectangleArea(heights))
