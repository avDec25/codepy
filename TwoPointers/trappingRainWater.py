from typing import List


class Solution:
    def trap(self, a: List[int]) -> int:
        n = len(a)
        left = [0] * n
        right = [0] * n

        left[0] = a[0]
        right[0] = a[n-1]

        for i in range(1, len(a)):
            left[i] = max(left[i-1], a[i])
            right[i] = max(right[i-1], a[n-i-1])
        right.reverse()

        ans = 0
        for i in range(n):
            ans += min(left[i], right[i]) - a[i]
        return ans


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(Solution().trap(height))

height = [4, 2, 0, 3, 2, 5]
print(Solution().trap(height))
