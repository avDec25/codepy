from typing import List


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def climb(n):
            if n < 0:
                return 0
            if n == 0:
                return 1
            if n in memo:
                return memo[n]
            memo[n] = climb(n - 1) + climb(n - 2)
            return memo[n]

        return climb(n)


    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return 0

        memo = {}

        def f(x):
            if x < 0:
                return -1
            if x == 0:
                return 0

            if x in memo:
                return memo[x]

            min_req = float("inf")
            for coin in coins:
                result = f(x - coin)
                if result != -1:
                    min_req = min(min_req, 1 + result)

            memo[x] = min_req
            return min_req

        ans = f(amount)
        if ans == float("inf"):
            return -1
        return ans


    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        T = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    T[i][j] = T[i - 1][j - 1] + 1
                else:
                    T[i][j] = max(T[i - 1][j], T[i][j - 1])

        return T[m][n]


    def knapsack(self, W: int, w: list[int], v: list[int]) -> int:
        n = len(w)
        T = [[0] * (W + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, W + 1):
                if w[i - 1] > j:
                    T[i][j] = T[i - 1][j]
                else:
                    T[i][j] = max(T[i - 1][j - w[i - 1]] + v[i - 1], T[i - 1][j])
        return T[n][W]


    def rob1(self, nums: List[int]) -> int:
        n = len(nums)


    # def rob2(self, nums: List[int]) -> int:
    # def rob3(self, root: Optional[TreeNode]) -> int:


print(2 == Solution().climbStairs(2))
print(3 == Solution().climbStairs(3))
print(3 == Solution().coinChange([1, 2, 5], 11))
print(-1 == Solution().coinChange([2], 3))
print(0 == Solution().coinChange([1], 0))

text1 = "abcde"
text2 = "ace"
print(Solution().longestCommonSubsequence(text1, text2) == 3)

text1 = "abc"
text2 = "abc"
print(Solution().longestCommonSubsequence(text1, text2) == 3)

text1 = "abc"
text2 = "def"
print(Solution().longestCommonSubsequence(text1, text2) == 0)

weights = [3, 4, 7]
values = [4, 5, 8]
max_weight = 7
print(Solution().knapsack(max_weight, weights, values) == 9)
