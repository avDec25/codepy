from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for e in nums:
            if e in seen:
                return True
            else:
                seen.add(e)
        return False


nums = [1,2,3,1]
print(Solution().containsDuplicate(nums))

nums = [1,2,3,4]
print(Solution().containsDuplicate(nums))

nums = [1,1,1,3,3,4,3,2,4,2]
print(Solution().containsDuplicate(nums))