from typing import List

import collections


class Solution:
    def maxSlidingWindow(self, a: List[int], k: int) -> List[int]:
        window = collections.deque(a[:k])
        curr_max = max(window)
        maxes = collections.deque([curr_max] * k)

        ans = [curr_max] * k
        for i in range(k, len(a)):
            if a[i] > curr_max:
                curr_max = a[i]
            ans.append(curr_max)
        return ans[k-1:]


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(Solution().maxSlidingWindow(nums, k))

nums = [1, -1]
k = 1
print(Solution().maxSlidingWindow(nums, k))
