from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[
        List[int]]:
        ans = set()

        def backtrack(temp, index, t):
            if t < 0:
                return

            if t == 0:
                ans.add(tuple(temp.copy()))
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]: continue
                temp.append(candidates[i])
                backtrack(temp, i+1, t - candidates[i])
                temp.pop()

        candidates.sort()
        backtrack([], 0, target)

        return [list(x) for x in ans]


candidates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
target = 30
print(Solution().combinationSum2(candidates, target))


candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(Solution().combinationSum2(candidates, target))


candidates = [2,5,2,1,2]
target = 5
print(Solution().combinationSum2(candidates, target))
