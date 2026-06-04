from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1 for _ in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

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
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        components = n
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    if uf.union(i, j):
                        components -= 1

        return components


isConnected = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]
print(Solution().findCircleNum(isConnected))

isConnected = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]
print(Solution().findCircleNum(isConnected))
