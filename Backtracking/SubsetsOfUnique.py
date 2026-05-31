from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtracking(i, a):
            if i == len(nums):
                ans.append(a.copy())
                return

            a.append(nums[i])
            backtracking(i+1, a)
            a.pop()
            backtracking(i+1, a)

        backtracking(0, [])
        return ans

nums = [1, 2, 3]
print(Solution().subsets(nums))

nums = [0]
print(Solution().subsets(nums))
