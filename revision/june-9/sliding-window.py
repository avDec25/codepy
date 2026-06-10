from typing import List
from collections import defaultdict, Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left, mx_len = 0, 0
        for right, cc in enumerate(s):
            if (cc in last_seen  # this makes the window invalid
                    and last_seen[cc] >= left):  # this means we have a correct window to look at
                left = last_seen[cc] + 1  # shift the window by jumping
            last_seen[cc] = right
            mx_len = max(mx_len, right - left + 1)
        return mx_len

    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        best = 0
        win_sum = 0
        freq = defaultdict(int)

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
                best = max(best, win_sum)

        return best

    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)
        required = len(need)
        have = {}
        formed = 0
        ans = (float("inf"), None, None)
        left = 0


        for right in range(len(s)):
            char_right = s[right]
            have[char_right] = have.get(char_right, 0) + 1

            if char_right in need and have[char_right] == need[char_right]:
                formed += 1

            while formed == required:
                win_size = right - left + 1
                if win_size < ans[0]:
                    ans = (win_size, left, right)

                char_left = s[left]
                have[char_left] -= 1
                if char_left in need and have[char_left] < need[char_left]:
                    formed -= 1
                left += 1

        if ans[0] == float("inf"):
            return ""
        return s[ans[1]:ans[2]+1]



s = "abcabcbb"
print(Solution().lengthOfLongestSubstring(s))

s = "bbbbb"
print(Solution().lengthOfLongestSubstring(s))

s = "pwwkew"
print(Solution().lengthOfLongestSubstring(s))

s = "ADOBECODEBANC"
t = "ABC"
print(Solution().minWindow(s, t))
