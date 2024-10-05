import collections
import itertools
from typing import List


class Solution:
    def canArrange(self, a: List[int], k: int) -> bool:
        freq = collections.defaultdict(int)
        for i in range(len(a)):
            mod = a[i] % k
            if mod >= 0:
                freq[mod] += 1
            else:
                freq[mod + k] += 1

        if freq[0] % 2 != 0:
            return False

        for i in range(1, k // 2 + 1):
            if freq[i] != freq[k - i]:
                return False

        return True


arr = [1, 2, 3, 4, 5, 10, 6, 7, 8, 9]
k = 5
print(Solution().canArrange(arr, k))

arr = [1, 2, 3, 4, 5, 6]
k = 7
print(Solution().canArrange(arr, k))

arr = [1, 2, 3, 4, 5, 6]
k = 10
print(Solution().canArrange(arr, k))
