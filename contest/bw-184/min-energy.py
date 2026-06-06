import math
class Solution:
    def minEnergy(self, n: int, brightness: int, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort()
        merged = []
        for start, end in intervals:
            if not merged:
                merged.append([start, end])
            else:
                prev_start, prev_end = merged[-1]
                if start <= prev_end + 1:
                    merged[-1][1] = max(prev_end, end)
                else:
                    merged.append([start, end])

        total_active_time = sum(end - start + 1 for start, end in merged)
        min_bulbs = math.ceil(brightness / 3)

        return min_bulbs * total_active_time


n = 5
brightness = 5
intervals = [[6, 12]]
print(Solution().minEnergy(n, brightness, intervals))

n = 2
brightness = 1
intervals = [[0, 0], [2, 2]]
print(Solution().minEnergy(n, brightness, intervals))

n = 4
brightness = 2
intervals = [[1, 3], [2, 4]]
print(Solution().minEnergy(n, brightness, intervals))
