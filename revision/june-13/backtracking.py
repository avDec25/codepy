from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(i, so_far):
            if i == len(nums):
                ans.append(so_far.copy())
                return

            so_far.append(nums[i])
            backtrack(i + 1, so_far)
            so_far.pop()
            backtrack(i + 1, so_far)

        backtrack(0, [])
        return ans

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        used = set()

        def backtrack(path):
            if len(path) == len(nums):
                ans.append(path.copy())
                return

            for num in nums:
                if num not in used:
                    used.add(num)

                    path.append(num)
                    backtrack(path)
                    path.pop()
                    backtrack(path)

                    used.remove(num)

        backtrack([])
        return ans

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:


candidates = [2, 3, 6, 7]
target = 7
print(Solution().combinationSum(candidates, target))

candidates = [2, 3, 5]
target = 8
print(Solution().combinationSum(candidates, target))

candidates = [2]
target = 1
print(Solution().combinationSum(candidates, target))
