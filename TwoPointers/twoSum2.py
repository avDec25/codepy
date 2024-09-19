from typing import List


class Solution:
    def twoSum(self, a: List[int], target: int) -> List[int]:
        n = len(a)
        i = 0
        j = n - 1
        while i < n and j > -1:
            sm = a[i] + a[j]
            if sm == target:
                return [i+1, j+1]
            elif sm > target:
                j -= 1
            else:
                i += 1
        return [i+1, j+1]


numbers = [2, 7, 11, 15]
target = 9
print(Solution().twoSum(numbers, target))

numbers = [2, 3, 4]
target = 6
print(Solution().twoSum(numbers, target))

numbers = [-1, 0]
target = -1
print(Solution().twoSum(numbers, target))
