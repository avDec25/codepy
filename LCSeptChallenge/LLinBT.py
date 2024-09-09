from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubPath(self, head: Optional[ListNode],
                  root: Optional[TreeNode]) -> bool:
        def check(head, root):
            if head is None: return True
            if root is None or head.val != root.val: return False
            return check(head.next, root.left) \
                or check(head.next, root.right)

        if root is None: return False
        if check(head, root): return True
        return self.isSubPath(head, root.left) \
            or self.isSubPath(head, root.right)


if __name__ == '__main__':
    tree = TreeNode(1)
    tree.left = TreeNode(4)
    tree.left.right = TreeNode(2)
    tree.left.right.left = TreeNode(1)
    tree.right = TreeNode(4)
    tree.right.left = TreeNode(2)
    tree.right.left.left = TreeNode(6)
    tree.right.left.right = TreeNode(8)
    tree.right.left.right.left = TreeNode(1)
    tree.right.left.right.right = TreeNode(3)

    ll = ListNode(1)
    ll.next = ListNode(4)
    ll.next.next = ListNode(2)
    ll.next.next.next = ListNode(6)

    print(Solution().isSubPath(ll, tree))
