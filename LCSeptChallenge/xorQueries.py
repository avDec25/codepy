from functools import lru_cache
from typing import List
class Solution:
    def xorQueries(self, a: List[int], q: List[List[int]]) -> List[int]:
        @lru_cache
        def getXor(l, r):
            temp = 0
            for i in range(l, r+1):
                temp ^= a[i]
            return temp

        ans = []
        for l, r in q:
            ans.append(getXor(l, r))
        return ans


arr = [1,3,4,8]
queries = [[0,1],[1,2],[0,3],[3,3]]
print(Solution().xorQueries(arr, queries))