from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(temp, index, target):
            if target < 0: return
            if target == 0:
                ans.append(temp.copy())
                return

            for i in range(index, len(candidates)):
                temp.append(candidates[i])
                backtrack(temp, i, target - candidates[i])
                temp.pop()

        backtrack([], 0, target)
        return ans


candidates = [2, 3, 6, 7]
target = 7
print(Solution().combinationSum(candidates, target))

candidates = [2, 3, 5]
target = 8
print(Solution().combinationSum(candidates, target))

candidates = [2]
target = 1
print(Solution().combinationSum(candidates, target))
