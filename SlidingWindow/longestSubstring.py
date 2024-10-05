class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l = 0
        seen = set()
        lss = 0
        for r in range(n):
            if s[r] not in seen:
                seen.add(s[r])
                lss = max(lss, r-l+1)
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                seen.add(s[r])
        return lss


s = "abcabcbb"
print(Solution().lengthOfLongestSubstring(s))

s = "bbbbb"
print(Solution().lengthOfLongestSubstring(s))

s = "pwwkew"
print(Solution().lengthOfLongestSubstring(s))
