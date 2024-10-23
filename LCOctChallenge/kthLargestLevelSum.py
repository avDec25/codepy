import collections
import heapq
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __repr__(self):
        return f"{self.val}"

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        q = collections.deque([root])
        while q:
            n = len(q)
            sm = 0
            while n:
                n -= 1
                popped = q.popleft()
                sm += popped.val
                if popped.left is not None:
                    q.append(popped.left)
                if popped.right is not None:
                    q.append(popped.right)
            heap.append(sm)

        return -1 if k > len(heap) else heapq.nlargest(k, heap)[-1]


k = 2
root = TreeNode(5)

root.left = TreeNode(8)
root.right = TreeNode(9)

root.right.left = TreeNode(3)
root.right.right = TreeNode(7)

root.left.left = TreeNode(2)
root.left.right = TreeNode(1)

root.left.left.left = TreeNode(4)
root.left.left.right = TreeNode(6)
print(Solution().kthLargestLevelSum(root, k))

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
print(Solution().kthLargestLevelSum(root, 1))
