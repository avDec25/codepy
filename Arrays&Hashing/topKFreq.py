from typing import List
import collections
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        heap = []
        for key in counter:
            heapq.heappush(heap, (counter[key], key))
        return [x[1] for x in heapq.nlargest(k, heap)]


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(Solution().topKFrequent(nums, k))

nums = [1]
k = 1
print(Solution().topKFrequent(nums, k))
