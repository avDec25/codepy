from typing import List


# class Solution:
#     def findMin(self, a: List[int]) -> int:
#         lo = 0
#         hi = len(a) - 1
#         ans = float('inf')
#         while lo <= hi:
#             mid = (hi + lo) // 2
#             if a[lo] <= a[hi]:
#                 ans = min(ans, a[lo])
#                 break
#
#             if a[lo] <= a[mid]:
#                 ans = min(ans, a[lo])
#                 lo = mid + 1
#             else:
#                 ans = min(ans, a[mid])
#                 hi = mid - 1
#
#         return ans

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        ans = float('inf')
        while left <= right:
            mid = left + (right - left) // 2
            if nums[left] <= nums[right]: # means arr is not rotated
                ans = min(ans, nums[left])
                break
            if nums[left] <= nums[mid]:
                ans = min(ans, nums[left])
                left = mid + 1
            else:
                ans = min(ans, nums[mid])
                right = mid - 1
        return ans


nums = [5, 1, 2, 3, 4]
print(Solution().findMin(nums))

nums = [3, 4, 5, 1, 2]
print(Solution().findMin(nums))

nums = [4, 5, 6, 7, 0, 1, 2]
print(Solution().findMin(nums))

nums = [11, 13, 15, 17]
print(Solution().findMin(nums))
