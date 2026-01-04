from typing import List


class Solution:
    def willComplete(self, time, mid, totalTrips):
        ans = 0
        for t in time:
            ans += mid // t
        return ans >= totalTrips

    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left = 1
        # although, worst case is max(time) * total trips
        # because question asks for minimum time to do all trips
        # So, upper bound = min(time) * totalTrips
        # as upper bound comes from the fastest bus
        right = min(time) * totalTrips
        while left < right:
            mid = left + (right - left) // 2
            if self.willComplete(time, mid, totalTrips):
                right = mid
            else:
                left = mid + 1
        return left


time = [1, 2, 3]
totalTrips = 5
print(Solution().minimumTime(time, totalTrips))

time = [2]
totalTrips = 1
print(Solution().minimumTime(time, totalTrips))
