# find depth of binary tree
# =========================
from collections import deque


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def dfsMaxDepth(node):
    if node is None: return 0
    l = dfsMaxDepth(node.left)
    r = dfsMaxDepth(node.right)
    return max(l, r) + 1


def bfsMaxDepth(node):
    if not node: return 0
    q = deque()
    q.append(node)
    h = 0

    while q:
        for _ in range(len(q)):
            temp = q.popleft()
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        h += 1

    return h


if __name__ == "__main__":
    root = Node(12)
    root.left = Node(8)
    root.right = Node(18)
    root.left.left = Node(5)
    root.left.right = Node(11)
    print(f"dfs = {dfsMaxDepth(root)}")
    print(f"bfs = {bfsMaxDepth(root)}")
