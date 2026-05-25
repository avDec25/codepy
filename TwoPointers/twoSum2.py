from typing import List


# in Theory the solution 1 should be faster that uses only two pointer approach
# and the second solution uses hash map, so there is an additional hash computation cost
# but however the LeetCode TwoSumII problem cases are
# the solution 2 came out to be much faster than two pointer approach

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pl = 0
        pr = len(nums) - 1

        while pl < pr:
            sm = nums[pl] + nums[pr]
            if sm == target:
                return [pl + 1, pr + 1]
            elif sm < target:
                pl += 1
            else:
                pr -= 1

        return []

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         mp = {}
#
#         for i, x in enumerate(nums):
#             complement = target - x
#             if complement in mp:
#                 # because complement already exists in mp
#                 # this means the index of complement occurred before the index of the current
#                 # as we are sequentially traversing the nums
#                 # and because we have to return response as index1 < index2
#                 # we do that like this:
#                 return [mp[complement]+1, i+1]
#             else:
#                 mp[x] = i
#
#         return []


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         mp = {}
#         for i in range(len(nums)):
#             complement = target - nums[i]
#             if complement in mp:
#                 return [mp[complement], i]
#             mp[nums[i]] = i
#         return []

numbers = [2, 7, 11, 15]
target = 9
print(Solution().twoSum(numbers, target))

numbers = [2, 3, 4]
target = 6
print(Solution().twoSum(numbers, target))

numbers = [-1, 0]
target = -1
print(Solution().twoSum(numbers, target))
