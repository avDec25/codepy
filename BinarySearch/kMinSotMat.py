from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        mx_heap = [] # max-heap of k size will have the kth min at top
        # merge-sorting: k-sorted arrays insertion in minheap


matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = 8

matrix = [[-5]]
k = 1
