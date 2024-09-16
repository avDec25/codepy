from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = sorted(
            int(time[:2]) * 60 + int(time[3:]) for time in timePoints
        )

        minutes.append(minutes[0] + 24 * 60)
        ans = minutes[-1]
        for i in range(1, len(minutes)):
            ans = min(ans, minutes[i] - minutes[i - 1])
        return ans


timePoints = ["23:59", "00:00", "00:00"]
print(Solution().findMinDifference(timePoints))
