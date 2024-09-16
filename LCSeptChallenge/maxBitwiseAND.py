from typing import List
from collections import defaultdict
from functools import lru_cache


class Solution:
    def __init__(self):
        self.a = None

    @lru_cache
    def bitwise_and(self, i, j):
        ans = self.a[i]
        for x in range(i + 1, j + 1):
            ans &= self.a[x]
        return ans

    def longestSubarray_v1(self, a: List[int]) -> int:
        self.a = a
        ss = defaultdict(list)
        mx_val = 0

        # BRUTE FORCE
        for i in range(len(self.a)):
            for j in range(i, len(self.a)):
                mx_cand = self.bitwise_and(i, j)
                if mx_cand >= mx_val:
                    mx_val = mx_cand
                    ss[mx_val].append(j - i + 1)

        return max(ss[mx_val])

    def longestSubarray(self, a: List[int]) -> int:
        max_val = max(a)
        max_index = a.index(max_val)

        ans, temp = 1, 1
        for i in range(max_index+1, len(a)):
            if a[i] == max_val:
                temp += 1
                ans = max(ans, temp)
            else:
                temp = 0
        return ans



if __name__ == '__main__':
    nums = [1, 2, 3, 3, 2, 2]
    print(Solution().longestSubarray(nums))

    nums = [1, 2, 3, 4]
    print(Solution().longestSubarray(nums))