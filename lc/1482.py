# 1482. Minimum Number of Days to Make m Bouquets
from typing import List


class Solution:
    def canMakeMBouquets(self, day, bloomDays, k):
        bouquets = 0
        consecutive = 0
        for bloomDay in bloomDays:
            if bloomDay <= day:
                consecutive += 1
            else:
                consecutive = 0

            if consecutive == k:
                bouquets += 1
                consecutive = 0

        return bouquets

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
            
        left = min(bloomDay)
        right = max(bloomDay)
        minDays = -1

        while left <= right:
            mid = left + (right - left) // 2
            if self.canMakeMBouquets(mid, bloomDay, k) >= m:
                minDays = mid
                right = mid - 1
            else:
                left = mid + 1
        return minDays


bloomDay = [1, 10, 3, 10, 2]
m = 3
k = 1
print(Solution().minDays(bloomDay, m, k))

bloomDay = [1, 10, 3, 10, 2]
m = 3
k = 2
print(Solution().minDays(bloomDay, m, k))

bloomDay = [7, 7, 7, 7, 12, 7, 7]
m = 2
k = 3
print(Solution().minDays(bloomDay, m, k))
