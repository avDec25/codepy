from typing import List


class Solution:
    def productExceptSelf(self, a: List[int]) -> List[int]:
        n = len(a)

        left = [a[0]]
        right = [a[n - 1]]

        for i in range(1, n):
            left.append(a[i] * left[i - 1])

        for j in range(n - 2, -1, -1):
            right.append(a[j] * right[n-j-2])
        right = right[::-1]

        # print(f"left {left}")
        # print(f"right {right}")

        ans = []
        for i in range(n):
            temp = 1
            if i - 1 >= 0:
                temp *= left[i - 1]

            if i + 1 < n:
                temp *= right[i + 1]
            ans.append(temp)

        return ans


nums = [1, 2, 3, 4]
print(Solution().productExceptSelf(nums))
print("===============================")
nums = [-1, 1, 0, -3, 3]
print(Solution().productExceptSelf(nums))
