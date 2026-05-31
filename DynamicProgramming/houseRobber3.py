from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def f(node):
            if not node:
                return 0, 0

            left = f(node.left)
            right = f(node.right)

            rob_this = node.val + left[1] + right[1]
            not_rob_this = max(left) + max(right)

            return rob_this, not_rob_this

        return max(f(root))
