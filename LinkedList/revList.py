from typing import Optional
from typing import List


# Definition for singly-linked list.
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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = None
        b = head
        while b:
            c = b.next
            b.next = a
            a = b
            b = c
        return a


head = [1, 2, 3, 4, 5]
listNode = create_linked_list(head)
print(Solution().reverseList(listNode))