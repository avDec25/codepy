from typing import List
import heapq


class Solution:
    def neighbours(self, u, v, R, C):
        ans = []
        for nx, ny in [(u + 0, v + 1), (u + 1, v + 0), (u - 1, v + 0),
                       (u + 0, v - 1)]:
            if 0 <= nx < R and 0 <= ny < C:
                ans.append((nx, ny))
        return ans

    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        R, C = len(grid), len(grid[0])
        end_point = (R - 1, C - 1)

        heap = [(grid[0][0], 0, 0)]

        visited = set()
        visited.add((0, 0))

        while heap:
            health_used, x, y = heapq.heappop(heap)

            if (x, y) == end_point:
                return True if health_used < health else False

            for a, b in self.neighbours(x, y, R, C):
                if (a, b) not in visited:
                    visited.add((a, b))
                    heapq.heappush(heap, (health_used + grid[a][b], a, b))

    def findSafeWalk_v2(self, grid: List[List[int]], health: int) -> bool:
        R, C = len(grid), len(grid[0])
        end_point = (R - 1, C - 1)

        visited = set()
        heap = [(grid[0][0], 0, 0)]

        while heap:
            health_used, x, y = heapq.heappop(heap)
            visited.add((x, y))

            if (x, y) == end_point:
                return True if health_used < health else False

            for a, b in self.neighbours(x, y, R, C):
                if (a, b) not in visited:
                    heapq.heappush(heap, (health_used + grid[a][b], a, b))


grid = [[1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0],
        [0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1],
        [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0],
        [1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1]]
health = 7
print(Solution().findSafeWalk_v2(grid, health))

grid = [[0, 1, 1, 0, 0, 0], [1, 0, 1, 0, 0, 0], [0, 1, 1, 1, 0, 1],
        [0, 0, 1, 0, 1, 0]]
health = 3
print(Solution().findSafeWalk_v2(grid, health))

grid = [[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]]
health = 1
print(Solution().findSafeWalk_v2(grid, health))
