import bisect


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                total = nums[i] + nums[lo] + nums[hi]

                if total < 0:
                    lo += 1
                elif total > 0:
                    hi -= 1
                else:
                    ans.append([nums[i], nums[lo], nums[hi]])

                    while lo < hi and nums[lo] == nums[lo + 1]:
                        lo += 1

                    while lo < hi and nums[hi] == nums[hi - 1]:
                        hi -= 1

                    lo += 1
                    hi -= 1

        return ans

    def merge_interval(self, intervals):
        intervals.sort()
        i = 0
        ans = []
        while i < len(intervals):
            s = intervals[i][0]
            e = intervals[i][1]
            while i < len(intervals) - 1 and e >= intervals[i + 1][0]:
                i += 1
                e = max(e, intervals[i][1])
            ans.append([s, e])
            i += 1

        return ans

    def insert_interval(self, intervals, newInterval):
        bisect.insort(intervals, newInterval)
        i = 0
        ans = []
        while i < len(intervals):
            s = intervals[i][0]
            e = intervals[i][1]
            while i < len(intervals) - 1 and e >= intervals[i+1][0]:
                i += 1
                e = max(e, intervals[i][1])
            ans.append([s,e])
            i += 1

        return ans


intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
print(Solution().insert_interval(intervals, newInterval))
intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]
print(Solution().insert_interval(intervals, newInterval))
