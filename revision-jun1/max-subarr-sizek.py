from collections import defaultdict
from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        win_sum = 0
        ans = 0

        for right in range(len(nums)):
            incoming = nums[right]
            freq[incoming] += 1
            win_sum += incoming

            if right >= k:
                outgoing = nums[right - k]
                freq[outgoing] -= 1
                win_sum -= outgoing
                
                if freq[outgoing] == 0:
                    del freq[outgoing]

            left = right - k + 1
            if left >= 0 and len(freq) == k:
                ans = max(ans, win_sum)
        
        return ans


nums = [1, 5, 4, 2, 9, 9, 9]
k = 3
print(Solution().maximumSubarraySum(nums, k))

nums = [4, 4, 4]
k = 3
print(Solution().maximumSubarraySum(nums, k))
