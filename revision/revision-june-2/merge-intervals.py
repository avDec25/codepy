import heapq
from bisect import insort
from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        i = 0
        ans = []
        while i < n:
            s = intervals[i][0]
            e = intervals[i][1]
            while i < n-1 and e >= intervals[i+1][0]:
                i += 1
                e = max(e, intervals[i][1])
            ans.append([s, e])
            i += 1
        return ans

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        insort(intervals, newInterval)
        i = 0
        n = len(intervals)
        while i < n:
            s = intervals[i][0]
            e = intervals[i][1]
            while i < n-1 and e >= intervals[i+1][0]:
                i += 1
                e = max(e, intervals[i][1]) # processed i+1 here
            ans.append([s,e])
            i += 1      # we have already processed i+1 above, so we can safely increment it here
        return ans

    def minMeetingRooms(self, intervals: List[Interval]) -> int: 
        if not intervals:
            return 0
        intervals.sort()
        heap = [intervals[0][1]]
        for s, e in intervals[1:]:
            if s >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, e)
        return len(heap)

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(Solution().merge(intervals))

intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(Solution().insert(intervals, newInterval))
