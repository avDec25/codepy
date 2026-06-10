import math
from typing import List


class Solution:
    def search(self, a: List[int], target: int) -> int:
        lo, hi = 0, len(a) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if a[mid] == target:
                return mid
            elif a[lo] <= a[mid]:  # left side already sorted
                if a[lo] <= target <= a[mid]:
                    hi -= 1
                else:
                    lo += 1
            else:
                if a[mid] <= target <= a[hi]:
                    lo += 1
                else:
                    hi -= 1
        return -1

    def findMin(self, a: List[int]) -> int:
        # min in rotated sorted
        lo, hi = 0, len(a) - 1
        ans = float("inf")
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if a[mid] < a[hi]:
                hi = mid
            else:
                lo = mid + 1
        return a[lo]

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(speed):
            return h >= sum(math.ceil(x / speed) for x in piles)
        lo = 1
        hi = max(piles)
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if can_finish(mid):
                hi = mid - 1
            else:
                lo = mid + 1
        return lo
