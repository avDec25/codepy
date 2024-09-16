from typing import List


class Solution:
    def backtrack(self, temp, cand, rem_sum, start):
        if rem_sum < 0:
            return
        elif rem_sum == 0:
            # copy not required because sorted already returns a copy of list,
            # not the list itself
            # self.ans.append(sorted(temp.copy()))
            self.ans.append(sorted(temp))

        for i in range(start, len(cand)):
            temp.append(cand[i])
            self.backtrack(temp, cand, rem_sum - cand[i], i)
            temp.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[
        List[int]]:
        self.ans = []
        self.backtrack([], list(set(candidates)), target, 0)
        return sorted(self.ans)

    def backtrack2(self, temp, cand, rem_sum, start):
        if rem_sum < 0: return
        elif rem_sum == 0: self.ans.append(temp.copy())

        for i in range(start, len(cand)):
            if i > start and cand[i] == cand[i-1]: continue
            temp.append(cand[i])
            self.backtrack2(temp, cand, rem_sum-cand[i], i+1)
            temp.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        self.backtrack2([], sorted(candidates), target, 0)
        return self.ans


if __name__ == '__main__':
    candidates = [10,1,2,7,6,1,5]
    target = 8
    for e in Solution().combinationSum2(candidates, target):
        print(e)
