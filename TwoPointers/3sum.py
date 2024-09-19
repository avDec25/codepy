from typing import List
from functools import lru_cache

class Solution:
    def threeSum(self, a: List[int]) -> List[List[int]]:
        n = len(a)
        a.sort()

        @lru_cache()
        def twoSum(target, index):
            ans = []
            i = 0
            j = n - 1
            while i < j:
                if i == index:
                    i += 1
                elif j == index:
                    j -= 1
                else:
                    temp = a[i] + a[j]
                    if temp == target:
                        ans.append([i, j])
                        i += 1
                        j -= 1
                    elif temp < target:
                        i += 1
                    else:
                        j -= 1
            return ans

        temp = set()
        for tindex in range(n):
            if tindex > 0 and a[tindex] == a[tindex-1]:
                continue
            ts = twoSum(-a[tindex], tindex)
            for e in ts:
                temp.add(tuple(sorted((a[tindex], a[e[0]], a[e[1]]))))
                
        return [list(e) for e in temp]


nums = [3, 0, -2, -1, 1, 2]
print(Solution().threeSum(nums))

nums = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(nums))

nums = [0, 1, 1]
print(Solution().threeSum(nums))

nums = [0, 0, 0]
print(Solution().threeSum(nums))
