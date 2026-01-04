from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        counter = {}
        
        for e in nums:
            if e != 0: prod *= e
            counter[e] = counter.get(e, 0) + 1

        ans = []
        if counter.get(0, 0) > 1:
            return [0 for _ in nums]
        elif counter.get(0) == 1:
            for e in nums:
                if e == 0:
                    ans.append(prod)
                else:
                    ans.append(0)
        else:
            for e in nums:
                ans.append(prod // e)
        
        return ans

        

nums = [1,2,3,4]
print(Solution().productExceptSelf(nums))
nums = [-1,1,0,-3,3]
print(Solution().productExceptSelf(nums))