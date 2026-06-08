from collections import defaultdict
from typing import List


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # two coloring
        color = [0 for _ in range(n + 1)]
        adj = defaultdict(list)
        for x, y in dislikes:
            adj[x].append(y)
            adj[y].append(x)

        def has_conflict(node, c):  # means, try coloring the node with new color c
            if color[node] != 0:
                return color[node] != c  # conflict arises if c is not same as existing color of node
            color[node] = c
            for neighbor in adj[node]:
                # neighbor should be in different color than c
                # chosen color here is -c (negative c)
                if has_conflict(neighbor, -c):
                    return True
            return False

        for i in range(1, n + 1):
            if color[i] == 0:
                if has_conflict(i, 1):
                    return False

        return True


n = 4
dislikes = [[1, 2], [1, 3], [2, 4]]
print(Solution().possibleBipartition(n, dislikes))

n = 3
dislikes = [[1, 2], [1, 3], [2, 3]]
print(Solution().possibleBipartition(n, dislikes))
