from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i, e in enumerate(nums):
            seen[e] = i

        for i, e in enumerate(nums):
            partner = target - e
            if partner in seen and i != seen[partner]:
                return [i, seen[partner]]



nums = [3, 2, 4]
target = 6
print(Solution().twoSum(nums, target))
