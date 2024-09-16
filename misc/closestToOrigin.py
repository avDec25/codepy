from typing import List
from heapq import heappush, nsmallest


class Solution:
    def distance(self, x, y):
        return pow(x, 2) + pow(y, 2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        heap = []
        for i, point in enumerate(points):
            heappush(heap, (self.distance(point[0], point[1]), i))

        for index in nsmallest(k, heap):
            ans.append(points[index[1]])

        return ans


points = [[1, 3], [-2, 2]]
k = 1
print(Solution().kClosest(points, k))

points = [[3,3],[5,-1],[-2,4]]
k = 2
print(Solution().kClosest(points, k))
