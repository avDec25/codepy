from typing import List


class Solution:
    def rotate(self, a: List[int], steps: int) -> None:
        n = len(a)
        for step in range(steps):
            save = a[n-1]
            for i in range(n-1, 0, -1):
                a[i] = a[i-1]
            a[0] = save


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
Solution().rotate(nums, k)
print(nums == [5, 6, 7, 1, 2, 3, 4])

nums = [-1, -100, 3, 99]
k = 2
Solution().rotate(nums, k)
print(nums == [3, 99, -1, -100])
