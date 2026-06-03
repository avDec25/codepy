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


# def connected_components(n, edges):
#     uf = UnionFind(n)
#     for


n = 5
edges = [[0,1],[1,2],[3,4]] # 2
print(connected_components(n, edges))
n = 5
edges = [[0,1],[1,2],[2,3],[3,4]] # 1
print(connected_components(n, edges))