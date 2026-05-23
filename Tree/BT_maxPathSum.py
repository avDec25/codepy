from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = -inf

        def maxpath(node: TreeNode):
            if node is None:
                return 0
            left_mx = max(0, maxpath(node.left))
            right_mx = max(0, maxpath(node.right))

            current_max = node.val + left_mx + right_mx
            self.max_sum = max(self.max_sum, current_max)

            return node.val + max(left_mx, right_mx)

        maxpath(root)
        return self.max_sum
