from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i, e in enumerate(nums):
            seen[e] = i

        for i, e in enumerate(nums):
            partner = target - e
            if partner in seen.keys() and i != seen[partner]:
                return [i, seen[partner]]
            
        return []

nums = [2,7,11,15]
target = 9
print(Solution().twoSum(nums, target))

nums = [3, 2, 4]
target = 6
print(Solution().twoSum(nums, target))

nums = [3,3]
target = 6
print(Solution().twoSum(nums, target))
