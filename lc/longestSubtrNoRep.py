class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_index = {}
        n = len(s)
        max_len = 0
        left = 0
        for right in range(n):
            c = s[right]
            if c in last_index:
                left = max(left, last_index[c])
            curr_len = right - left + 1
            if curr_len > max_len:
                max_len = curr_len
            last_index[c] = right + 1
        return max_len


s = "abcabcbb"
print(Solution().lengthOfLongestSubstring(s))

s = "bbbbb"
print(Solution().lengthOfLongestSubstring(s))

s = "pwwkew"
print(Solution().lengthOfLongestSubstring(s))
