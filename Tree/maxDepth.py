# find depth of binary tree
# =========================
# from collections import deque
#
#
# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None
#
#
# def dfsMaxDepth(node):
#     if node is None: return 0
#     l = dfsMaxDepth(node.left)
#     r = dfsMaxDepth(node.right)
#     return max(l, r) + 1
#
#
# def bfsMaxDepth(node):
#     if not node: return 0
#     q = deque()
#     q.append(node)
#     h = 0
#
#     while q:
#         for _ in range(len(q)):
#             temp = q.popleft()
#             if temp.left:
#                 q.append(temp.left)
#             if temp.right:
#                 q.append(temp.right)
#         h += 1
#
#     return h


from typing import Optional


class TreeNode:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

    def __repr__(self):
        print(self.data)


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1


if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(8)
    root.right = TreeNode(18)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(11)
    print(Solution().maxDepth(root))

# if __name__ == "__main__":
#     root = Node(12)
#     root.left = Node(8)
#     root.right = Node(18)
#     root.left.left = Node(5)
#     root.left.right = Node(11)
#     print(f"dfs = {dfsMaxDepth(root)}")
#     print(f"bfs = {bfsMaxDepth(root)}")
