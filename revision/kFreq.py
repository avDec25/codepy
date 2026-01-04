from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = Counter(nums)
        heap = []
        for val, count in freq.items():
            heapq.heappush(heap, (count, val))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [val for _, val in heap]