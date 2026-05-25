from collections import defaultdict


class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        ans = []
        freq = defaultdict()
        for i, e in enumerate(nums):
            if freq.get(e, 0) < k:
                freq[e] = freq.get(e, 0) + 1
                ans.append(e)

        return ans

nums = [1, 1, 1, 2, 2, 3]
k = 2
print(Solution().limitOccurrences(nums, k))

nums = [1, 2, 3]
k = 1
print(Solution().limitOccurrences(nums, k))
