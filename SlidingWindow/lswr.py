class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        mx_len = 0

        for right, cc in enumerate(s):
            if cc in last_seen and last_seen[cc] >= left:
                left = last_seen[cc] + 1
            last_seen[cc] = right
            mx_len = max(mx_len, right-left+1)

        return mx_len


s = "abcabcbb"
print(Solution().lengthOfLongestSubstring(s))

s = "bbbbb"
print(Solution().lengthOfLongestSubstring(s))

s = "pwwkew"
print(Solution().lengthOfLongestSubstring(s))
