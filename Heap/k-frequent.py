import heapq
from collections import Counter
from typing import List


class Solution:
    # O(n log k)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)  # O(n)
        heap = []

        # since size of heap is never allowed to go beyond k
        # so insertion in heap will cost O(log k) only
        for n, freq in counts.items():
            heapq.heappush(heap, (freq, n))
            if len(heap) > k:
                heapq.heappop(heap)

        # building ans = O(k)
        return [heap[i][1] for i in range(k)]


nums = [5, 2, 5, 3, 5, 3, 1, 1, 3]
k = 2
print(Solution().topKFrequent(nums, k))

nums = [3, 0, 1, 0]
k = 1
print(Solution().topKFrequent(nums, k))

nums = [1]
k = 1
print(Solution().topKFrequent(nums, k))

nums = [1, 2, 1, 2, 1, 2, 3, 1, 3, 2]
k = 2
print(Solution().topKFrequent(nums, k))
