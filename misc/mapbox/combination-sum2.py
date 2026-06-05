from collections import defaultdict
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:



candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(Solution().combinationSum2(candidates, target))

candidates = [2, 5, 2, 1, 2]
target = 5
print(Solution().combinationSum2(candidates, target))
