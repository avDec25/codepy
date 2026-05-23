class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root

        while curr:
            # dono he greater hai to right depth mei aur ja sakte hai, aur least sakte hai in depth
            if p.val > curr.val and q.val > curr.val:  # means both in right subtree, we can go in lower levels
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val: # means both in left subtree, we can go in lower levels
                curr = curr.left
            else:
                return curr
        return None