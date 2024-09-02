from collections import deque


class Solution:
    def findOrder(self, n, m, prerequisites):
        q = deque()
        order = []

        inDeg = [0] * n
        adj = [[] for _ in range(n)]
        for u, v in prerequisites:
            adj[v].append(u)
            inDeg[u] += 1

        for u in range(n):
            if inDeg[u] == 0:
                q.append(u)

        while q:
            popped = q.popleft()
            order.append(popped)
            for neighbour in adj[popped]:
                inDeg[neighbour] -= 1
                if inDeg[neighbour] == 0:
                    q.append(neighbour)
        return order if len(order) == n else []


if __name__ == '__main__':
    n = 25
    m = 14
    prerequisites = [[10, 18],
                     [0, 18],
                     [10, 6],
                     [16, 0],
                     [8, 7],
                     [19, 15],
                     [24, 16],
                     [20, 14],
                     [1, 17],
                     [14, 13],
                     [21, 21],
                     [19, 22],
                     [23, 20],
                     [10, 5]]

    print(Solution().findOrder(n, m, prerequisites))
