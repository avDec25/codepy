import heapq
from collections import defaultdict
from typing import List


class Solution:

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, delay in times:
            adj[u].append((v, delay))

        visited = set()
        heap = [(0, k)]

        while heap:
            curr_delay, popped = heapq.heappop(heap)
            visited.add(popped)

            if len(visited) == n:
                return curr_delay

            for neighbour, dd in adj[popped]:
                if neighbour not in visited:
                    heapq.heappush(heap, (dd+curr_delay, neighbour))

        return -1


times = [[1, 2, 10],
         [1, 3, 5],
         [2, 3, 2],
         [2, 4, 1],
         [3, 2, 3],
         [3, 4, 9],
         [3, 5, 2],
         [4, 5, 4],
         [5, 4, 6],
         [5, 1, 7]]
n = 5
k = 1
print(Solution().networkDelayTime(times, n, k))
