from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return self.val


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        The diameter of a binary tree is the length of the longest path
        between any two nodes in the tree.
        That path doesn’t have to pass through the root.
        """
        self.diameter = 0

        def height(node: TreeNode):
            if not node: return 0

            left_height = height(node.left)
            right_height = height(node.right)

            self.diameter = max(self.diameter, left_height + right_height)
            return 1 + max(left_height,  right_height)

        height(root)
        return self.diameter

if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(8)
    root.right = TreeNode(18)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(11)
    print(Solution().diameterOfBinaryTree(root))
