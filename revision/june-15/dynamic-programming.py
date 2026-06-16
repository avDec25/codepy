from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def climb(steps):
            if steps in memo:
                return memo[steps]

            if steps < 0:
                return 0

            if steps == 0:
                return 1

            memo[steps] = climb(steps - 1) + climb(steps - 2)
            return memo[steps]

        return climb(n)

    def coinChange(self, coins: List[int], amount: int) -> int:
        def f(x):
            if x < 0:
                return -1
            if x == 0:
                return 0
            min_req = float("inf")
            for coin in coins:
                temp = f(x - coin)
                if temp != -1:
                    min_req = min(min_req, temp + 1)
            return min_req

        ans = f(amount)
        if ans == float("inf"):
            return -1
        return ans

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)

        dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[n1][n2]

    def knapsack(W: int, w: list[int], v: list[int]) -> int:
        n = len(w)
        dp = [[0 for _ in range(W + 1)] for _ in range(n)]

        for i in range(1, n + 1):
            for j in range(1, W + 1):
                if w[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], v[i - 1] + dp[i - 1][j - w[i - 1]])

        return dp[n][W]

    def rob(self, nums: List[int]) -> int:
        memo = {}

        def solve(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            memo[i] = max(solve(i + 1), solve(i + 2) + nums[i])
            return memo[i]

        return solve(0)

    def rob2(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def solve(i, a: List[int]):
            if i >= len(a):
                return 0
            if i in memo:
                return memo[i]
            memo[i] = max(solve(i + 1, a), solve(i + 2, a) + a[i])
            return memo[i]

        memo = {}
        nil = solve(0, nums[:-1])
        memo = {}
        nif = solve(0, nums[1:])
        return max(nil, nif)

    def rob(self, root: Optional[TreeNode]) -> int:
        def f(node):
            if not node:
                return 0, 0

            left = f(node.left)
            right = f(node.right)
            rob_this = node.val + left[1] + right[1]
            not_rob_this = max(left) + max(right)

            return rob_this, not_rob_this

        return max(f(root))


nums = [2, 3, 2]
print(Solution().rob2(nums))

nums = [1, 2, 3, 1]
print(Solution().rob2(nums))

nums = [1, 2, 3]
print(Solution().rob2(nums))
