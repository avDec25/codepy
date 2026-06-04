from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1 for _ in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # Union by Size
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False

        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        self.size[rx] += self.size[ry]
        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def component_size(self, x):
        return self.size[self.find(x)]


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n)
        for u, v in edges:
            if not uf.union(u-1, v-1):
                return [u, v]
        return []

edges = [[1, 2], [1, 3], [2, 3]]
print(Solution().findRedundantConnection(edges))

edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
print(Solution().findRedundantConnection(edges))
