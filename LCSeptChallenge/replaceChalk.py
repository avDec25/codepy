from typing import List

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k = k % sum(chalk)
        for i, c in enumerate(chalk):
            if k-c >= 0:
                k -= c
            else:
                return i

chalk = [3,4,1,2]
k = 25
print(Solution().chalkReplacer(chalk, k))