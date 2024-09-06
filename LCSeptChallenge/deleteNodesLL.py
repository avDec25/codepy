from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> \
            Optional[ListNode]:
        prev = None
        ptr = head
        while ptr:
            if ptr.val in nums:
                if prev is None:
                    head = head.next
                    ptr = ptr.next
                    continue
                prev.next = ptr.next
            else:
                prev = ptr
            ptr = ptr.next

        # printList(head)
        return head


def printList(head: Optional[ListNode]):
    if head is None:
        print("Empty List")
        return
    ptr = head
    while ptr:
        print(f"({ptr.val}) -> ", end='')
        ptr = ptr.next
    print("")


if __name__ == '__main__':
    nums = [1]
    head = [1, 2, 1, 2, 1, 2]

    nums = [5]
    head = [1, 2, 3, 4]

    nums = [1, 2, 3]
    head = [1, 2, 3, 4, 5]

    ll = ListNode(1)
    temp = ll
    for i in range(1, len(head)):
        temp.next = ListNode(head[i])
        temp = temp.next

    printList(ll)
    Solution().modifiedList(nums, ll)
