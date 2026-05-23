import heapq
from typing import List

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         heap = []
#         for x in nums:
#             heapq.heappush(heap, x)
#             if len(heap) > k:
#                 heapq.heappop(heap)
#         return heap[0]


class Solution:
    def findKthLargest(self, nums: List[int], k: int):
        print(heapq.nlargest(k, nums))
        # return heapq.nlargest(k, nums)[-1]


nums = [3, 2, 1, 5, 6, 4]
k = 2
print(Solution().findKthLargest(nums, k))

nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
print(Solution().findKthLargest(nums, k))
