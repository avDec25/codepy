import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode()
        tail = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         heap = []
#         # we need the extra i
#         # there because the tuple comparison will move to next element in case of draw b/w [0]th element
#         # but 'i' will always be distinct and comparison will stop there
#         # TypeError: '<' not supported between instances of 'ListNode' and 'ListNode'
#         for i, node in enumerate(lists):
#             if node:
#                 heappush(heap, (node.val, i, node))
#
#         dummy_head = ListNode()
#         tail = dummy_head
#
#         while heap:
#             val, i, node = heappop(heap)
#             tail.next = node
#             tail = tail.next
#             if node.next:
#                 heappush(heap, (node.next.val, i, node.next))
#
#         return dummy_head.next