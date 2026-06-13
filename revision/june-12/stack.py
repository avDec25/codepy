from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0 for _ in range(n)]
        stk = []
        for i in range(n):
            while stk and temperatures[i] > temperatures[stk[-1]]:
                index = stk.pop()
                ans[index] = i - index
            stk.append(i)
        return ans

    def largestRectangleArea(self, heights):
        stk = [0]
        heights.append(0)
        ans = 0
        for i in range(len(heights)):
            while stk and heights[i] < heights[stk[-1]]:
                ht = heights[stk.pop()]
                if not stk:
                    wd = i
                else:
                    wd = i - stk[-1] - 1
                ans = max(ans, ht*wd)
            stk.append(i)
        return ans

heights = [2,1,5,6,2,3]
print(Solution().largestRectangleArea(heights))

heights = [2,4]
print(Solution().largestRectangleArea(heights))
