from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}

        def find(x):
            # "If x has never been seen before, set parent[x] = x and return x."
            # "If x has been seen before, return parent[x]."
            if parent.setdefault(x, x) != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[ry] = rx

        for r, c in stones:
            union(r, ~c)

        # from a component we can keep removing until one remains, because all other are connected
        # either by row or column,
        # AND it's a property of graph that we can remove all nodes until 1 remains
        num_components = len(set(find(x) for x in parent))
        return len(stones) - num_components


class Solution2:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry: return False
            parent[ry] = rx
            return True

        def can_connect(i, j):
            r1, c1 = stones[i]
            r2, c2 = stones[j]
            return r1 == r2 or c1 == c2

        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if can_connect(i, j) and union(i, j):
                    ans += 1
        return ans


class Solution3:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}
        size = {}

        def find(x):
            if parent.setdefault(x, x) != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            if size.setdefault(rx, 1) < size.setdefault(ry, 1):
                rx, ry = ry, rx
            parent[ry] = rx
            size[rx] += size[ry]
            return True

        for r, c in stones:
            union(r, ~c)

        num_unique_components = len(set(find(x) for x in parent))
        return len(stones) - num_unique_components


stones = [[0, 0], [0, 1],
          [1, 0], [1, 2],
          [2, 1], [2, 2]]
print(Solution().removeStones(stones))

stones = [[0, 0], [0, 2],
          [1, 1],
          [2, 0], [2, 2]]
print(Solution().removeStones(stones))

stones = [[0, 0]]
print(Solution().removeStones(stones))
