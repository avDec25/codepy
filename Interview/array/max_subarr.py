from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = mx_sum = nums[0]
        for e in nums[1:]:
            
            # add the next element to the current arr to add to max subarr sum,
            # or start a new arr from curr element
            curr_sum = max(curr_sum + e, e)
            
            mx_sum = max(mx_sum, curr_sum)
        return mx_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray(nums))

nums = [1]
print(Solution().maxSubArray(nums))

nums = [5,4,-1,7,8]
print(Solution().maxSubArray(nums))
