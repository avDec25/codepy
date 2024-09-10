from typing import Optional
from math import gcd


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"({self.val}) --> "


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> \
    Optional[ListNode]:
        ptr = head
        prev = ptr
        ptr = ptr.next
        while ptr:
            prev.next = ListNode(gcd(prev.val, ptr.val))
            prev.next.next = ptr
            prev = ptr
            ptr = ptr.next
        return head


def printLL(head: Optional[ListNode]):
    ptr = head
    while ptr:
        print(ptr, end='')
        ptr = ptr.next


if __name__ == '__main__':
    head = ListNode(18)
    head.next = ListNode(6)
    head.next.next = ListNode(10)
    head.next.next.next = ListNode(3)
    ll = Solution().insertGreatestCommonDivisors(head)
    printLL(ll)
