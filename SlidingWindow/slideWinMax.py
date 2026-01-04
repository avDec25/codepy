from collections import deque
from typing import List


# import collections
#
# class Solution:
#     def maxSlidingWindow(self, a: List[int], k: int) -> List[int]:
#         window = collections.deque(a[:k])
#         curr_max = max(window)
#         maxes = collections.deque([curr_max] * k)
#
#         ans = [curr_max] * k
#         for i in range(k, len(a)):
#             if a[i] > curr_max:
#                 curr_max = a[i]
#             ans.append(curr_max)
#         return ans[k - 1:]


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        ans = []

        for i, e in enumerate(nums):
            while dq and e >= nums[dq[-1]]:
                dq.pop()

            dq.append(i)

            # check if dq[0] is not a valid index, means permissible in the sliding window
            if dq[0] <= i - k:
                dq.popleft()

            # append answer only when we have a window
            # i+1 is number of elements parsed, as we are at the i-index
            if i + 1 >= k:
                ans.append(nums[dq[0]])
        return ans


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(Solution().maxSlidingWindow(nums, k))

nums = [1, -1]
k = 1
print(Solution().maxSlidingWindow(nums, k))
