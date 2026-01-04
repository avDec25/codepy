from typing import List


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        min_n = float('inf')
        max_n = float('-inf')
        seen = set()
        for x in nums:
            min_n = min(min_n, x)
            max_n = max(max_n, x)
            seen.add(x)

        ans = []
        for i in range(min_n, max_n+1):
            if i not in seen:
                ans.append(i)

        return sorted(ans)



nums = [1, 4, 2, 5]
print(Solution().findMissingElements(nums))

nums = [7, 8, 6, 9]
print(Solution().findMissingElements(nums))

nums = [5, 1]
print(Solution().findMissingElements(nums))
