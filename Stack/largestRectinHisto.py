from typing import List


class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        stk = [(0, h[0])]
        area_max = 0
        for i, ht in enumerate(h):
            start = i
            while stk and h[i] < stk[-1][1]:
                pi, ph = stk.pop()
                area_max = max(area_max, (i - pi) * ph)
                start = pi
            stk.append((start, ht))

        for i, ht in stk:
            area_max = max(area_max, ht * (len(h) - i))

        return area_max


heights = [2, 1, 5, 6, 2, 3]
print(Solution().largestRectangleArea(heights))

heights = [2, 4]
print(Solution().largestRectangleArea(heights))
