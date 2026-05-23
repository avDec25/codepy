from typing import List, Optional


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


def create_linked_list(arr: List[int]) -> ListNode:
    if not arr:
        return None
    prev = None
    for i in range(len(arr) - 1, -1, -1):
        curr = ListNode(arr[i])
        curr.next = prev
        prev = curr
    return prev


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy
        for _ in range(n + 1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next

head = [1, 2, 3, 4, 5]
n = 2
head = create_linked_list(head)
print(Solution().removeNthFromEnd(head, n))

head = [1]
n = 1
head = create_linked_list(head)
print(Solution().removeNthFromEnd(head, n))

head = [1, 2]
n = 1
head = create_linked_list(head)
print(Solution().removeNthFromEnd(head, n))


