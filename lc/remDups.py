from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        write = 2
        for read in range(2, n):
            if nums[read] != nums[write-2]:
                nums[write] = nums[read]
                write += 1
        return write

nums = [1, 1, 1, 2, 2, 3]
print(Solution().removeDuplicates(nums))
print(nums)

nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
print(Solution().removeDuplicates(nums))
print(nums)
