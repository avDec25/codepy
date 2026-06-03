from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        stk = [(root, 0)]
        while stk:
            top, sum_so_far = stk.pop()
            if top.left:
                stk.append((top.left, sum_so_far + top.val))
            if top.right:
                stk.append((top.right, sum_so_far + top.val))
            if top.left is None and top.right is None:
                if sum_so_far + top.val == targetSum:
                    return True
        return False

    def hasPathSumRecursive(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, sm):
            if not node:
                return False

            if node.left is None and node.right is None:
                return sm+node.val == targetSum

            return dfs(node.left, node.val+sm) or dfs(node.right, node.val+sm)

        return dfs(root, 0)