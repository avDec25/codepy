from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        used = set()

        def backtrack(curr):
            if len(curr) == len(nums):
                ans.append(curr.copy())
                return

            for num in nums:
                if num in used:
                    continue

                curr.append(num)
                used.add(num)

                backtrack(curr)

                curr.pop()
                used.remove(num)


        backtrack([])
        return ans


nums = [1, 2, 3]
print(Solution().permute(nums))

nums = [0, 1]
print(Solution().permute(nums))

nums = [1]
print(Solution().permute(nums))
