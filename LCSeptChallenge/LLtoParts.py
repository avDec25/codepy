from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        ans = ""
        ptr = self
        while ptr:
            ans += f"({ptr.val}) --> "
            ptr = ptr.next
        return ans


class Solution:

    def sizeof(self, head: Optional[ListNode]):
        if not head: return 0
        ptr = head
        size = 0
        while ptr:
            ptr = ptr.next
            size += 1
        return size

    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[ \
            Optional[ListNode]]:
        parts = []
        n = self.sizeof(head)

        if n < k:
            parts = [0 for _ in range(k)]
            for i in range(n):
                parts[i] += 1
        else:
            for i in range(k):
                parts.append(n // k)
            for i in range(n % k):
                parts[i] += 1
        # print(parts)

        ll = []
        ptr = head
        for e in parts:
            i = 0
            ll.append(ptr)
            while ptr:
                prev = ptr
                ptr = ptr.next
                i += 1
                if i == e:
                    prev.next = None
                    break
        return ll


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    # head.next.next.next = ListNode(4)
    # head.next.next.next.next = ListNode(5)
    # head.next.next.next.next.next = ListNode(6)
    # head.next.next.next.next.next.next = ListNode(7)
    # head.next.next.next.next.next.next.next = ListNode(8)
    # head.next.next.next.next.next.next.next.next = ListNode(9)
    # head.next.next.next.next.next.next.next.next.next = ListNode(10)
    print(head)
    k = 5
    ll = Solution().splitListToParts(head, k)
    print(ll)
    # for e in ll:
    #     print(e)
