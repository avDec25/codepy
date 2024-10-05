import itertools
from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        def backtrack(temp, index):
            ans.append(temp.copy())
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]: continue
                temp.append(nums[i])
                backtrack(temp, i+1)
                temp.pop()

        backtrack([], 0)
        return ans

    def subsetsWithDup_v1(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        for i in range(len(nums)+1):
            for x in itertools.combinations(nums, i):
                ans.add(x)

        return [list(x) for x in ans]


nums = [1, 2, 2]
print(Solution().subsetsWithDup(nums))

nums = [4,4,4,1,4]
print(Solution().subsetsWithDup(nums))
