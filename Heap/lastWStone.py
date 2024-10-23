import heapq
from typing import List
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) > 1:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, -(y-x))

        if heap:
            return -heap[0]
        else:
            return 0


stones = [2,7,4,1,8,1]
print(Solution().lastStoneWeight(stones))

stones = [1]
print(Solution().lastStoneWeight(stones))
