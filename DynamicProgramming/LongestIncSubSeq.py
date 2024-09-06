# length of longest increasing subsequence
import bisect


class Solution:

    # slower
    def dpLiss(self, a):
        ans = 0
        dp = [1 for _ in range(len(a))]
        dp[len(a) - 1] = 1
        for i in range(len(a) - 2, -1, -1):
            for j in range(i + 1, len(a)):
                if a[j] > a[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            ans = max(dp[i], ans)
        return ans

    # faster, another solution
    def liss(self, a):
        ans = 0
        dp = [1 for _ in range(len(a))]
        prev_list = [(a[0], 1)]

        for i in range(1, len(a)):
            index = bisect.bisect_left(prev_list, (a[i], 1))
            for j in range(index-1, -1, -1):
                if prev_list[j][0] < a[i] and dp[i] < (prev_list[j][1]+1):
                    dp[i] = max(dp[i], prev_list[j][1] + 1)
            bisect.insort(prev_list, (a[i], dp[i]))
            ans = max(ans, dp[i])
        return ans


if __name__ == '__main__':
    # a = [10, 22, 9, 33, 21, 50, 41, 60]
    a = [10, 10, 9, 8, 4, 8, 10, 4, 5, 12, 12, 7]
    print(Solution().dpLiss(a))
    print(Solution().liss(a))
