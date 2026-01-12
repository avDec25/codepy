from typing import Optional
from typing import List


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
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1: return l2
        if not l2: return l1

        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

list1 = [1, 2, 4]
list2 = [1, 3, 4]
print(Solution().mergeTwoLists(create_linked_list(list1), create_linked_list(list2)))
