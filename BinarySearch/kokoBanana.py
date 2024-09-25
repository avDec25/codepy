import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def timeToEatAll(k):
            t = 0
            for e in piles:
                t += math.ceil(e / k)
            return t

        lo = 1
        hi = max(piles)

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            tte = timeToEatAll(mid)

            if tte > h:
                lo = mid + 1
            else:
                hi = mid - 1

        return lo


piles = [312884470]
h = 312884469
print(Solution().minEatingSpeed(piles, h))

piles = [3, 6, 7, 11]
h = 8
print(Solution().minEatingSpeed(piles, h))

piles = [30, 11, 23, 4, 20]
h = 5
print(Solution().minEatingSpeed(piles, h))

piles = [30, 11, 23, 4, 20]
h = 6
print(Solution().minEatingSpeed(piles, h))
