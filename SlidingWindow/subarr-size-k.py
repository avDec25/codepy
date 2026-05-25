from typing import List
from collections import defaultdict


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        window_sum = 0
        best = 0

        for right in range(len(nums)):
            incoming = nums[right]
            freq[incoming] += 1
            window_sum += incoming

            if right >= k:
                outgoing = nums[right - k]
                freq[outgoing] -= 1
                window_sum -= outgoing

                if freq[outgoing] == 0:
                    del freq[outgoing]

            left = right - k + 1
            if left >= 0 and len(freq) == k:
                best = max(best, window_sum)

        return best


nums = [1, 5, 4, 2, 9, 9, 9]
k = 3
print(Solution().maximumSubarraySum(nums, k))

nums = [4, 4, 4]
k = 3
print(Solution().maximumSubarraySum(nums, k))
