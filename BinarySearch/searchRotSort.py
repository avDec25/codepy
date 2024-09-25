from typing import List


class Solution:
    def search(self, a: List[int], target: int) -> int:
        lo = 0
        hi = len(a) - 1

        while lo <= hi:
            mid = (hi + lo) // 2
            if a[mid] == target:
                return mid
            elif a[lo] <= a[mid]:   # (lo to mid) is continuously increasing
                if a[lo] <= target <= a[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if a[mid] <= target <= a[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1


nums = [3, 5, 1]
target = 3
print(Solution().search(nums, target))

nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(Solution().search(nums, target))

nums = [4, 5, 6, 7, 0, 1, 2]
target = 3
print(Solution().search(nums, target))

nums = [1]
target = 0
print(Solution().search(nums, target))
