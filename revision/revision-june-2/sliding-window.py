from collections import Counter
from collections import defaultdict
from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        mx_len = 0
        left = 0

        for right, cc in enumerate(s):
            if right in last_seen and left <= last_seen[cc]:
                left = last_seen[cc] + 1
            last_seen[cc] = right
            mx_len = max(mx_len, right - left + 1)

        return mx_len

    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        win_sum = 0
        mx_sum = 0
        freq = defaultdict(int)
        
        for right in range(len(nums)):
            incoming = nums[right]
            freq[incoming] += 1
            win_sum += incoming
            
            if right >= k:
                outgoing = nums[right-k]
                freq[outgoing] -= 1
                win_sum -= outgoing
                
                if freq[outgoing] == 0:
                    del freq[outgoing]
                
            left = right - k + 1
            if left >= 0 and len(freq) == k:
                mx_sum = max(mx_sum, win_sum)
            
        return mx_sum

    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        required = len(need)
        left, right, formed = 0, 0, 0
        have = defaultdict(int)

        ans = (float("inf"), None, None)
        while right < len(s):
            char_right = s[right]
            have[char_right] += 1

            if char_right in need and have[char_right] == need[char_right]:
                formed += 1

            while left <= right and required == formed:
                win_size = right - left + 1
                if win_size < ans[0]:
                    ans = (win_size, left, right)

                char_left = s[left]
                have[char_left] -= 1

                if char_left in need and have[char_left] < need[char_left]:
                    formed -= 1

                left += 1

            right += 1

        if ans[0] == float('inf'):
            return ""
        return s[ans[1] : ans[2] + 1]
