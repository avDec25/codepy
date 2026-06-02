class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        ans, left = 0, 0
        for right, cc in enumerate(s):
            if cc in last_seen and left <= last_seen[cc]:
                left = last_seen[cc] + 1
            last_seen[cc] = right
            ans = max(ans, right - left + 1)
        return ans



s = "abcabcbb"
print(Solution().lengthOfLongestSubstring(s))

s = "bbbbb"
print(Solution().lengthOfLongestSubstring(s))

s = "pwwkew"
print(Solution().lengthOfLongestSubstring(s))
