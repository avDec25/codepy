from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def traverseSpiral(self, R, C, a, head):

        top, bottom, left, right = 0, R - 1, 0, C - 1

        while top <= bottom and left <= right:

            for i in range(left, right + 1):
                if head is not None:
                    a[top][i] = head.val
                    head = head.next
            top += 1

            for i in range(top, bottom + 1):
                if head is not None:
                    a[i][right] = head.val
                    head = head.next
            right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    if head is not None:
                        a[bottom][i] = head.val
                        head = head.next
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    if head is not None:
                        a[i][left] = head.val
                        head = head.next
                left += 1

    def spiralMatrix(self, R: int, C: int, head: Optional[ListNode]) -> List[
        List[int]]:
        a = [[-1 for _ in range(C)] for _ in range(R)]
        self.traverseSpiral(R, C, a, head)
        return a


if __name__ == '__main__':
    R = 3
    C = 5
    head = ListNode(3)
    head.next = ListNode(0)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(6)
    head.next.next.next.next = ListNode(8)
    head.next.next.next.next.next = ListNode(1)
    head.next.next.next.next.next.next = ListNode(7)
    head.next.next.next.next.next.next.next = ListNode(9)
    head.next.next.next.next.next.next.next.next = ListNode(4)
    head.next.next.next.next.next.next.next.next.next = ListNode(2)
    head.next.next.next.next.next.next.next.next.next.next = ListNode(5)
    head.next.next.next.next.next.next.next.next.next.next.next = ListNode(5)
    head.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(
        0)

    print(Solution().spiralMatrix(R, C, head))
