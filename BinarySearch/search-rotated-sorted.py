from typing import List


class Solution:
    def search(self, a: List[int], target: int) -> int:
        l, r = 0, len(a) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if a[mid] == target:
                return mid

            elif a[l] <= a[mid]:
                if a[l] <= target <= a[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                # l takes the place of mid in next iteration
                # to reduce search space
                # normal way of binary search
                if a[mid] <= target <= a[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1



nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(Solution().search(nums, target))

nums = [4, 5, 6, 7, 0, 1, 2]
target = 3
print(Solution().search(nums, target))

nums = [1]
target = 0
print(Solution().search(nums, target))
