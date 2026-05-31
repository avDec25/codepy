class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        mx_area = 0
        heights.append(0)

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                ht = heights[stack.pop()]
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                mx_area = max(mx_area, ht * width)
            stack.append(i)

        return mx_area


heights = [2, 1, 5, 6, 2, 3]
print(Solution().largestRectangleArea(heights))

# heights = [2, 4]
# print(Solution().largestRectangleArea(heights))
