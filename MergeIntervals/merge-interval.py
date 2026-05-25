from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i = 0
        ans = []
        intervals.sort()
        while i < len(intervals):
            s = intervals[i][0]
            e = intervals[i][1]

            while i < len(intervals) - 1 and e >= intervals[i+1][0]:
                i += 1
                # e = max(current_farthest_right, new_interval_right)
                e = max(e, intervals[i][1])

            ans.append([s, e])
            i += 1

        return ans

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(Solution().merge(intervals))

intervals = [[1, 4], [4, 5]]
print(Solution().merge(intervals))

intervals = [[4, 7], [1, 4]]
print(Solution().merge(intervals))
