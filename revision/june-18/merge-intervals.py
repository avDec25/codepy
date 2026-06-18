from typing import List
from bisect import insort
from heapq import heappush, heappop


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i = 0
        ans = []
        intervals.sort()
        while i < len(intervals):
            s = intervals[i][0]
            e = intervals[i][1]
            while i < len(intervals) - 1 and e >= intervals[i + 1][0]:
                i += 1
                e = max(e, intervals[i][1])
            ans.append([s, e])
            i += 1
        return ans

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        insort(intervals, newInterval)
        ans = []
        i = 0
        while i < len(intervals):
            s = intervals[i][0]
            e = intervals[i][1]
            while i < len(intervals) - 1 and e >= intervals[i + 1][0]:
                i += 1
                e = max(e, intervals[i][1])
            ans.append([s, e])
            i += 1
        return ans

    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key = lambda x: x.start)
        heap = [intervals[0].end]

        for interval in intervals[1:]:
            s = interval.start
            e = interval.end
            if s >= heap[0]:
                heappop(heap)

            heappush(heap, e)

        return len(heap)


intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
print(Solution().insert(intervals, newInterval))

intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]
print(Solution().insert(intervals, newInterval))
