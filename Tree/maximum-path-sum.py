from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def mx_path(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left_mx_sum  = max(0, mx_path(node.left))
            right_mx_sum = max(0, mx_path(node.right))
            
            curr_max = node.val + left_mx_sum + right_mx_sum
            
            self.max_sum = max(self.max_sum, curr_max)
            
            return node.val + max(left_mx_sum, right_mx_sum)

        mx_path(root)
        return self.max_sum



if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(2)
    root.right = TreeNode(10)
    root.left.left = TreeNode(20)
    root.left.right = TreeNode(1)
    root.right.right = TreeNode(-25)
    root.right.right.left = TreeNode(3)
    root.right.right.right = TreeNode(4)

    # root = TreeNode(-25)
    # root.left = TreeNode(3)
    # root.right = TreeNode(4)

    print(Solution().maxPathSum(root))
