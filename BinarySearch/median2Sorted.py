import heapq
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int],
                               nums2: List[int]) -> float:
        left = []   # max-heap
        right = []  # min-heap

        def median(element):
            heapq.heappush(left, -element)
            heapq.heappush(right, -heapq.heappop(left))

            # we keep the left, greater than 1 or equal
            if len(left) < len(right):
                heapq.heappush(left, -heapq.heappop(right))

            if len(left) == len(right):
                return (-left[0] + right[0])/2
            else:
                return -left[0]

        m = len(nums1)
        n = len(nums2)
        i, j = 0, 0
        curr_median = None
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                curr_median = median(nums1[i])
                i += 1
            else:
                curr_median = median(nums2[j])
                j += 1

        while i < m:
            curr_median = median(nums1[i])
            i += 1
        while j < n:
            curr_median = median(nums2[j])
            j += 1

        return curr_median


nums1 = [1, 3]
nums2 = [2]
print(Solution().findMedianSortedArrays(nums1, nums2))

nums1 = [1, 2]
nums2 = [3, 4]
print(Solution().findMedianSortedArrays(nums1, nums2))
