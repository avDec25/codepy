from heapq import heappop, heappush
from typing import List, Counter, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for x in nums:
            heappush(heap, x)
            if len(heap) > k:
                heappop(heap)
        return heap[0]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        for item, f in freq.items():
            heappush(heap, (f, item))
            if len(heap) > k:
                heappop(heap)

        return [item for f, item in heap]

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        # we need the extra i
        # there because the tuple comparison will move to next element in case of draw b/w [0]th element
        # but 'i' will always be distinct and comparison will stop there
        # TypeError: '<' not supported between instances of 'ListNode' and 'ListNode'
        for i, node in enumerate(lists):
            if node:
                heappush(heap, (node.val, i, node))

        dummy_head = ListNode()
        tail = dummy_head

        while heap:
            val, i, node = heappop(heap)
            tail.next = node
            tail = tail.next
            if node.next:
                heappush(heap, (node.next.val, i, node.next))

        return dummy_head.next