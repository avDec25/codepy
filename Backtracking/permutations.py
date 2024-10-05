import itertools
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        # for x in itertools.permutations(nums):
        #     ans.append(x)
        # return ans

        def backtrack(temp):
            if len(temp) == len(nums):
                ans.append(temp.copy())
                return

            for i in range(len(nums)):
                if nums[i] in temp:
                    continue
                temp.append(nums[i])
                backtrack(temp)
                temp.pop()

        backtrack([])
        return ans


nums = [1, 2, 3]
print(Solution().permute(nums))
