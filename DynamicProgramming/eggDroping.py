from functools import lru_cache
import sys


class Solution:
    calls = set()
    cCount = 0

    def superEggDrop(self, e: int, f: int) -> int:
        dp = [[100000 for _ in range(f + 1)] for _ in range(e + 1)]
        for i in range(1, e + 1):
            dp[i][0] = 0
            dp[i][1] = 1
        for j in range(1, f + 1):
            dp[1][j] = j

        for i in range(2, e + 1):
            for j in range(2, f + 1):
                # for x in range(1, j + 1):
                #     trials = 1 + max(dp[i - 1][x - 1], dp[i][j - x])
                #     dp[i][j] = min(dp[i][j], trials)
                # Replaced by Binary search
                lo = 1
                hi = j
                while lo <= hi:
                    mid = lo + (hi - lo) // 2
                    left = dp[i - 1][mid - 1]
                    right = dp[i][j - mid]
                    trials = 1 + max(left, right)
                    if left < right:
                        lo = mid + 1
                    else:
                        hi = mid - 1
                    dp[i][j] = min(trials, dp[i][j])

        return dp[e][f]

    def superEggDrop_v2(self, e: int, f: int) -> int:
        dp = [[100000 for _ in range(f + 1)] for _ in range(e + 1)]
        for i in range(1, e + 1):
            dp[i][0] = 0
            dp[i][1] = 1
        for j in range(1, f + 1):
            dp[1][j] = j

        for i in range(2, e + 1):
            for j in range(2, f + 1):
                for x in range(1, j + 1):
                    trials = 1 + max(dp[i - 1][x - 1], dp[i][j - x])
                    dp[i][j] = min(dp[i][j], trials)

        return dp[e][f]

    @lru_cache  # memoization
    def superEggDropRec(self, e: int, k: int) -> int:
        self.calls.add((e, k))
        self.cCount += 1
        if k == 0 or k == 1: return k
        if e == 1: return k

        ans = float('inf')
        for f in range(1, k + 1):
            trials = 1 + max(self.superEggDropRec(e - 1, f - 1),
                             self.superEggDropRec(e, k - f))
            ans = min(trials, ans)
        return ans

    def printUniqueCalls(self):
        print(len(self.calls))
        print(self.cCount)
        print(self.calls)


e = 7
f = 5812
sol = Solution()
print(sol.superEggDrop(e, f))
# print(sol.superEggDrop_v2(e, f))
# print(sol.superEggDropRec(e, f))
# sol.printUniqueCalls()
