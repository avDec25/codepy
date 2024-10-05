from typing import List


class Solution:
    def subsets(self, a: List[int]) -> List[List[int]]:
        ans = []

        def genSubset(temp, i):
            ans.append(temp.copy())
            for j in range(i, len(a)):
                temp.append(a[j])
                genSubset(temp, j + 1)
                temp.pop()

        genSubset([], 0)
        return ans


nums = [1, 2, 3]
print(Solution().subsets(nums))

nums = [0]
print(Solution().subsets(nums))
