# K Closest Points to Origin
import heapq
from typing import List


class Solution:
    def distance(self, x, y):
        return pow(x, 2) + pow(y, 2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i, point in enumerate(points):
            heapq.heappush(heap, (-self.distance(point[0], point[1]), i))
            if len(heap) > k:
                heapq.heappop(heap)

        ans = []
        for d, i in heap:
            ans.append(list(points[i]))

        return ans


points = [[1, 3], [-2, 2]]
k = 1
print(Solution().kClosest(points, k))

points = [[3, 3], [5, -1], [-2, 4]]
k = 2
print(Solution().kClosest(points, k))
