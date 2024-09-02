from typing import List
import heapq


class Solution:
    def minCost(self, a: List[int]) -> int:
        total_min_cost = 0
        heapq.heapify(a)
        while len(a) != 1:
            fmin = heapq.heappop(a)
            smin = heapq.heappop(a)

            cost = fmin + smin
            total_min_cost += cost

            heapq.heappush(a, cost)
        return total_min_cost



if __name__ == '__main__':
    arr = [4, 3, 2, 6]
    print(Solution().minCost(arr))
