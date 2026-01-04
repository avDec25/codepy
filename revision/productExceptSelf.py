class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        prefix_product = 1

        for i in range(len(nums)):
            answer[i] = prefix_product
            prefix_product *= nums[i]

        suffix_product = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= suffix_product
            suffix_product *= nums[i]
        
        return answer