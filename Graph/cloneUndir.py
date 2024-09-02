from collections import deque
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, root: Optional['Node']) -> Optional['Node']:
        if root:
            m = {}
            q = deque()
            m[root] = Node(root.val)
            q.append(root)
            while q:
                popped = q.popleft()
                for neighbour in popped.neighbors:
                    if neighbour not in m:
                        m[neighbour] = Node(neighbour.val)
                        q.append(neighbour)
                    m[popped].neighbors.append(m[neighbour])
            return m[root]

    def traversal(self, root: Optional['Node']):
        m = set()
        q = deque()
        m.add(root)
        q.append(root)

        while q:
            popped = q.popleft()
            print(popped.val)
            for neighbor in popped.neighbors:
                if neighbor not in m:
                    m.add(neighbor)
                    q.append(neighbor)


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node3, node1]
    cloned = Solution().cloneGraph(node1)
    Solution().traversal(node1)
    print("=========")
    Solution().traversal(cloned)
