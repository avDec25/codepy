from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_to_new = {}

        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]

            # create copy of value
            copy = Node(node.val)
            old_to_new[node] = copy

            # create copy of neighbors
            for nei in node.neighbors:
                # on return of this DFS the edge is formed
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node)
