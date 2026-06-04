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
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)
        components = n
        redundant = 0
        for u, v in edges:
            if uf.union(u, v):
                components -= 1
            else:
                redundant += 1
                break

        return redundant == 0 and components == 1



n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
print(Solution().validTree(n, edges))

n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
print(Solution().validTree(n, edges))
