class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        mx_length = 0

        for right in range(len(s)):
            curr_char = s[right]
            if curr_char in last_seen and last_seen[curr_char] >= left:
                left = last_seen[curr_char] + 1
            last_seen[curr_char] = right
            mx_length = max(mx_length, right - left + 1)

        return mx_length

s = "abcabcbb"
print(Solution().lengthOfLongestSubstring(s))

s = "bbbbb"
print(Solution().lengthOfLongestSubstring(s))

s = "pwwkew"
print(Solution().lengthOfLongestSubstring(s))
