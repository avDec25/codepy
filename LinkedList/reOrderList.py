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
    def reverse_list(self, head: ListNode) -> ListNode:
        if not head:
            return None
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow is now the middle
        second = slow.next
        slow.next = None

        # this means we not have two lists
        # head -> ... -> slow
        # second -> ... -> end

        # now reverse the second list
        second = self.reverse_list(second)

        # simply merge the first half and the second reversed half
        first = head
        while second:
            nxt1 = first.next
            nxt2 = second.next

            first.next = second
            second.next = nxt1

            first = nxt1
            second = nxt2


head = [1, 2, 3, 4]
head = create_linked_list(head)
Solution().reorderList(head)
print(head)

head = [1, 2, 3, 4, 5]
head = create_linked_list(head)
Solution().reorderList(head)
print(head)
