from typing import List
import heapq


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort()
        # number of rooms required
        min_heap = [intervals[0][1]]

        for s, e in intervals[1:]:

            # room becomes free we pop it
            if s >= min_heap[0]:
                heapq.heappop(min_heap)

            # then we push the last meeting end time to the heap
            # so that we keep the information in min_heap that 1 room was required for prior meeting
            # i.e. the last meeting end time
            heapq.heappush(min_heap, e)

        return len(min_heap)


intervals = [(0, 40), (5, 10), (15, 20)]
print(Solution().minMeetingRooms(intervals))

intervals = [(4, 9)]
print(Solution().minMeetingRooms(intervals))
