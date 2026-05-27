from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        mx_sum = -inf

        def mps(node):
            nonlocal mx_sum

            if node is None:
                return 0

            left_sum = max(0, mps(node.left))
            right_sum = max(0, mps(node.right))

            mx_sum = max(mx_sum, node.val + left_sum + right_sum)
            return node.val + max(left_sum, right_sum)

        mps(root)
        return mx_sum
