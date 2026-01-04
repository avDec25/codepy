class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i, val in enumerate(nums):
            complement = target - val
            if complement in mp:
                return [i, mp[complement]]
            mp[nums[i]] = i
        return []