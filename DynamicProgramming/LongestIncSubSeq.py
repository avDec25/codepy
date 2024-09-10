# length of longest increasing subsequence
from typing import List
import math

import time


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"{func.__name__} took {elapsed_time:.6f} seconds")
        return result

    return wrapper


class Solution:

    # slower
    @timing_decorator
    def dpLiss(self, a):
        ans = 0
        dp = [1 for _ in range(len(a))]
        for i in range(len(a) - 2, -1, -1):
            for j in range(i + 1, len(a)):
                if a[j] > a[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            ans = max(dp[i], ans)
        return ans

    # faster, another solution
    @timing_decorator
    def lengthOfLIS(self, a: List[int]) -> int:
        piles = [[math.inf]]
        for x in a:
            inserted = False
            for pile in piles:
                if pile[-1] >= x:
                    pile.append(x)
                    inserted = True
                    break
            if not inserted:
                piles.append([x])
        return len(piles)


if __name__ == '__main__':
    a = [10, 22, 9, 33, 21, 50, 41, 60]
    # a = [10, 10, 9, 8, 4, 8, 10, 4, 5, 12, 12, 7]
    print(Solution().dpLiss(a))
    print(Solution().lengthOfLIS(a))
