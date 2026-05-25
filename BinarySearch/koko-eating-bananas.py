from typing import List
from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(speed):
            return h >= sum(
                [ceil(x / speed) for x in piles]
            )

        lo = 1
        hi = max(piles)
        while lo <= hi:
            mid = (hi + lo) // 2
            if can_finish(mid):
                hi = mid - 1
            else:
                lo = mid + 1

        return lo


piles = [3, 6, 7, 11]
h = 8
print(Solution().minEatingSpeed(piles, h))

piles = [30, 11, 23, 4, 20]
h = 5
print(Solution().minEatingSpeed(piles, h))

piles = [30, 11, 23, 4, 20]
h = 6
print(Solution().minEatingSpeed(piles, h))
