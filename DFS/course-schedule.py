from collections import deque
from typing import List


class Solution:

    # dfs with back-edge detection
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        state = [0] * numCourses

        for u, v in prerequisites:
            graph[v].append(u)

        def has_cycle(node):
            if state[node] == 2:
                return False

            if state[node] == 1:
                return True

            state[node] = 1
            for nei in graph[node]:
                if has_cycle(nei):
                    return True
            state[node] = 2

            return False

        for i in range(numCourses):
            if has_cycle(i):
                return False

        return True

    # khan's algorithm: topological sorting
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        for u, v in prerequisites:
            graph[v].append(u)
            in_degree[u] += 1

        q = deque([i for i in range(numCourses) if in_degree[i] == 0])
        taken = 0

        while q:
            u = q.popleft()
            taken += 1
            for nei in graph[u]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)

        return taken == numCourses


numCourses = 8
prerequisites = [[1, 7], [1, 2], [6, 1], [2, 0], [0, 3], [6, 4], [5, 6], [5, 4]]
print(Solution().canFinish(numCourses, prerequisites))

numCourses = 2
prerequisites = [[1, 0]]
print(Solution().canFinish(numCourses, prerequisites))

numCourses = 2
prerequisites = [[1, 0], [0, 1]]
print(Solution().canFinish(numCourses, prerequisites))
