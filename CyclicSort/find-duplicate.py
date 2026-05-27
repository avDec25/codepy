from typing import List


# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         slow = nums[0]
#         fast = nums[nums[0]]
#
#         while slow != fast:
#             slow = nums[slow]
#             fast = nums[nums[fast]]
#
#         slow = 0
#         while slow != fast:
#             slow = nums[slow]
#             fast = nums[fast]
#
#         return slow


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Floyd’s algorithm requires the pointers to move before comparison
        # they should not be equal when starting
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow = 0
        # finding entrance of the cycle
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


nums = [1, 3, 4, 2, 2]
print(Solution().findDuplicate(nums))

nums = [3, 1, 3, 4, 2]
print(Solution().findDuplicate(nums))

nums = [3, 3, 3, 3, 3]
print(Solution().findDuplicate(nums))
