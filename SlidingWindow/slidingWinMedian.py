from typing import List
from sortedcontainers import SortedList


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        result = []
        window = SortedList()
        for i in range(k):
            window.add(nums[i])

        def get_median():
            if k % 2 == 1:
                return float(window[k // 2])
            else:
                return (window[k // 2] + window[k // 2 - 1]) / 2.0

        result.append(get_median())

        for i in range(k, len(nums)):
            window.remove(nums[i - k])
            window.add(nums[i])

            result.append(get_median())

        return result


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(Solution().medianSlidingWindow(nums, k))

nums = [1, 2, 3, 4, 2, 3, 1, 4, 2]
k = 3
print(Solution().medianSlidingWindow(nums, k))
