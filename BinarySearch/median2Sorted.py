from heapq import heappush, heappop
from typing import List


# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int],
#                                nums2: List[int]) -> float:
#         left = []  # max-heap
#         right = []  # min-heap
#
#         def median(element):
#             heapq.heappush(left, -element)
#             heapq.heappush(right, -heapq.heappop(left))
#
#             # we keep the left, greater than 1 or equal
#             if len(left) < len(right):
#                 heapq.heappush(left, -heapq.heappop(right))
#
#             if len(left) == len(right):
#                 return (-left[0] + right[0]) / 2
#             else:
#                 return -left[0]
#
#         m = len(nums1)
#         n = len(nums2)
#         i, j = 0, 0
#         curr_median = None
#         while i < m and j < n:
#             if nums1[i] < nums2[j]:
#                 curr_median = median(nums1[i])
#                 i += 1
#             else:
#                 curr_median = median(nums2[j])
#                 j += 1
#
#         while i < m:
#             curr_median = median(nums1[i])
#             i += 1
#         while j < n:
#             curr_median = median(nums2[j])
#             j += 1
#
#         return curr_median


# this solution will also work for unsorted array
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        left = []  # max-heap
        right = []  # min-heap

        def median(element):
            # we are assuming that both are equal in size, so keeping that property
            heappush(left, -element)
            heappush(right, -heappop(left))

            if len(left) < len(right):
                heappush(left, -heappop(right))

            if len(left) == len(right):
                return (-left[0] + right[0]) / 2
            else:
                return -left[0]

        n1 = len(nums1)
        n2 = len(nums2)

        i = 0
        j = 0
        curr_median = None
        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                curr_median = median(nums1[i])
                i += 1
            else:
                curr_median = median(nums2[j])
                j += 1

        while i < n1:
            curr_median = median(nums1[i])
            i += 1

        while j < n2:
            curr_median = median(nums2[j])
            j += 1

        return curr_median



nums1 = [1, 3]
nums2 = [2]
print(Solution().findMedianSortedArrays(nums1, nums2))

nums1 = [1, 2]
nums2 = [3, 4]
print(Solution().findMedianSortedArrays(nums1, nums2))
