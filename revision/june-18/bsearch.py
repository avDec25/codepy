import math
from typing import List


class Solution:
    def search(self, a: List[int], target: int) -> int:
        lo, hi = 0, len(a) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if target == a[mid]:
                return mid

            if a[lo] <= a[mid]:
                if a[lo] <= target <= a[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if a[mid] <= target <= a[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return -1


    def findMin(self, a: List[int]) -> int:
        lo, hi = 0, len(a) - 1
        # terminate when 1 element remain
        while lo < hi: # as soon as the search space shrinks to a single element
            mid = lo + (hi - lo) // 2
            if a[mid] < a[hi]:
                hi = mid
            else:
                lo = mid + 1
        return a[lo]


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(speed):
            return h >= sum([math.ceil(x // speed) for x in piles])

        lo, hi = 0, len(piles)
        # terminate when 0 elements remain
        while lo <= hi: # search until active range is completely empty
            mid = lo + (hi - lo) // 2
            if can_finish(mid):
                hi = mid - 1
            else:
                lo = mid + 1
        return lo


nums = [3, 4, 5, 1, 2]
print(Solution().findMin(nums))

nums = [4, 5, 6, 7, 0, 1, 2]
print(Solution().findMin(nums))

nums = [11, 13, 15, 17]
print(Solution().findMin(nums))
