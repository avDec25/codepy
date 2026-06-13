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
                ans = max(ans, ht * wd)
            stk.append(i)
        return ans

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_grtr = {}
        stk = []
        for x in reversed(nums2):
            while stk and stk[-1] <= x:
                stk.pop()
            next_grtr[x] = -1 if not stk else stk[-1]
            stk.append(x)
        return [next_grtr[x] for x in nums1]

    def nextGreaterElements(self, nums):
        next_grtr = []
        for i in range(len(nums)):
            found = False
            for x in nums[i + 1:] + nums[:i]:
                if nums[i] < x:
                    next_grtr.append(x)
                    found = True
                    break
            if not found:
                next_grtr.append(-1)
        return next_grtr


nums = [1, 2, 1]
print(Solution().nextGreaterElements(nums))

nums = [1, 2, 3, 4, 3]
print(Solution().nextGreaterElements(nums))
