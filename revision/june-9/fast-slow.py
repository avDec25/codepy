from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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
        mp = set()
        while True:
            if n in mp:
                break
            mp.add(n)
            sm = 0
            while n:
                rem = n % 10
                sm += rem ** 2
                n //= 10
            n = sm
            if n == 1:
                return True

        return False

n = 19
print(Solution().isHappy(n))
n = 2
print(Solution().isHappy(n))