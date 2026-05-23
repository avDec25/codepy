from typing import Optional


class TreeNode:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

    def __repr__(self):
        print(self.data)


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(8)
    root.right = TreeNode(18)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(11)
    print(Solution().invertTree(root))
