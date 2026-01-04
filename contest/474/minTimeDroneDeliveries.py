from typing import List
from math import lcm


class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        d1, d2 = d
        r1, r2 = r

        def feasible(t):
            d1_available = t - (t // r1)
            d2_available = t - (t // r2)

            # both drones not available at lcm(r1, r2)
            atleast_one_available = t - (t // lcm(r1, r2))
            return d1_available >= d1 and d2_available >= d2 and atleast_one_available >= sum(d)

        # assuming no recharges at all, min slots required
        low = sum(d)
        # worst case: a drone after each delivery requires a recharge, r_i = 2,
        # and there are two drones
        high = 2 * low * 2

        ans = high
        while low <= high:
            mid = low + (high - low) // 2
            if feasible(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans


d = [3, 1]
r = [2, 3]
print(Solution().minimumTime(d, r))

d = [1, 3]
r = [2, 2]
print(Solution().minimumTime(d, r))

d = [2, 1]
r = [3, 4]
print(Solution().minimumTime(d, r))
