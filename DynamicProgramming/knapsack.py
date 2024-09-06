from typing import List


def knapsack01(W: int, profit: List[int], weight: List[int]):
    dp = [[0 for _ in range(W + 1)] for _ in range(len(weight) + 1)]

    for r in range(1, len(weight) + 1):  # bag-weights
        for c in range(1, W + 1):  # article-weights
            if weight[r - 1] > c:
                dp[r][c] = dp[r-1][c]
            else:
                dp[r][c] = max(dp[r-1][c], profit[r-1] + dp[r-1][c-weight[r-1]])
    return dp[len(weight)][W]


weight = [1, 3, 4, 5]
profit = [1, 4, 5, 7]
W = 7
print(knapsack01(W, profit, weight))
