import bisect
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        bisect.insort(intervals, newInterval)
        ans = []

        i = 0
        while i < len(intervals):
            s = intervals[i][0]
            e = intervals[i][1]
            while i < len(intervals) - 1 and e >= intervals[i + 1][0]:
                i += 1
                e = max(e, intervals[i][1])
            ans.append([s, e])
            i += 1  # we have already processed i+1 here, so safe to do this

        return ans


intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
print(Solution().insert(intervals, newInterval))

intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]
print(Solution().insert(intervals, newInterval))
