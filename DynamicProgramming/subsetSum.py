# Does there exists a subset such that the sum of which equals given target
from typing import List


def subsets(a: List[int], target: int) -> bool:
    dp = [[False for _ in range(target + 1)] for _ in range(len(a) + 1)]

    for j in range(len(a) + 1):
        dp[0][j] = True

    for i in range(1, len(a) + 1):
        for j in range(1, target + 1):
            if j - a[i - 1] >= 0:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - a[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[len(a)][target]


a = [3, 34, 4, 12, 5, 2]
target = 10
print(subsets(a, target))
