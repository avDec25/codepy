from typing import List
from collections import deque


# Khan's algorithm for topological sorting
# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         graph = [[] for _ in range(numCourses)]
#         in_degree = [0]*numCourses
#
#         for course, pre in prerequisites:
#             graph[pre].append(course)
#             in_degree[course] += 1
#
#         q = deque([i for i in range(numCourses) if in_degree[i] == 0])
#
#         taken = 0
#         while q:
#             u = q.popleft()
#             taken += 1
#             for v in graph[u]:
#                 in_degree[v] -= 1
#                 if in_degree[v] == 0:
#                     q.append(v)
#
#         return taken == numCourses

# Graph Colouring + DFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            graph[pre].append(course)

        state = [0] * numCourses

        def dfs(u):
            if state[u] == 1:
                return False  # means cycle found
            if state[u] == 2:
                return True  # means all ok no cycle found

            state[u] = 1
            for nei in graph[u]:
                if not dfs(nei):
                    return False
            state[u] = 2

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True

    # def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    #     graph = [[] for _ in range(numCourses)]
    #     for course, pre in prerequisites:
    #         graph[pre].append(course)
    #
    #     # 0 = unvisited
    #     # 1 = visiting
    #     # 2 = visited
    #     state = [0] * numCourses
    #
    #     # return True if it contains cycle
    #     def dfs(u):
    #         # if visiting a node we come across another one which is being visiting already
    #         # this means we have hit a cycle, so returning False
    #         if state[u] == 1:
    #             return False
    #
    #         if state[u] == 2:
    #             # reached a dead end, no cycles from here, so return True
    #             return True
    #
    #         state[u] = 1
    #         for v in graph[u]:
    #             if not dfs(v):
    #                 return False
    #         state[u] = 2
    #
    #         return True
    #
    #
    #     for i in range(numCourses):
    #         if state[i] == 0:
    #             if not dfs(i):
    #                 return False
    #
    #     return True
