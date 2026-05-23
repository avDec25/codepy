from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        repr = ""
        head = self
        while head:
            repr += f"({head.val}) -> "
            head = head.next

        return repr


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                x_ptr = head  # covers x
                z_ptr = fast  # covers z
                while x_ptr != z_ptr:
                    x_ptr = x_ptr.next
                    z_ptr = z_ptr.next
                return x_ptr

        return None