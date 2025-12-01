from typing import List


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left = min(time) * totalTrips
        right = max(time) * totalTrips
        ans = left
        while left < right:
            mid = left + (right - left) // 2
            


time = [1, 2, 3]
totalTrips = 5
print(Solution().minimumTime(time, totalTrips))

time = [2]
totalTrips = 1
print(Solution().minimumTime(time, totalTrips))
