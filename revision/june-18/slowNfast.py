from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def isHappy(self, n: int) -> bool:
        mp = {}

        def sq_sum(x):
            result = 0
            while x:
                rem = x % 10
                result += rem ** 2
                x //= 10
            return result

        while True:
            if n in mp:
                return False
            else:
                hn = sq_sum(n)
                mp[n] = hn
                n = hn
            if hn == 1:
                return True


n = 19
print(Solution().isHappy(n))

n = 2
print(Solution().isHappy(n))
