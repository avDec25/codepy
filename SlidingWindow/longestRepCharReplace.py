import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        freq = collections.defaultdict(int)
        mxf = 0
        ans = 0
        n = len(s)
        for r in range(n):
            freq[s[r]] += 1
            mxf = max(mxf, freq[s[r]])
            while (r-l+1)-mxf > k:
                freq[s[l]] -= 1
                l += 1
            ans = max(ans, r-l+1)
        return ans


s = "ABAB"
k = 2
print(Solution().characterReplacement(s, k))

s = "AABABBA"
k = 1
print(Solution().characterReplacement(s, k))
