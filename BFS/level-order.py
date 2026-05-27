from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# [3,9,20,null,null,15,7]
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        q = deque([root])

        while q:
            n = len(q)
            level = []
            while n:
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                n -= 1
            ans.append(level)
        return ans
