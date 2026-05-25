from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        required = len(need)
        left, right, formed = 0, 0, 0
        have = {}

        ans = (float('inf'), None, None)
        while right < len(s):
            char_right = s[right]
            have[char_right] = have.get(char_right, 0) + 1

            if char_right in need and need[char_right] == have[char_right]:
                formed += 1

            while left <= right and formed == required:
                win_size = right - left + 1
                if win_size < ans[0]:
                    ans = (win_size, left, right)

                char_left = s[left]
                left += 1
                have[char_left] -= 1
                if char_left in need and have[char_left] < need[char_left]:
                    formed -= 1
            right += 1

        if ans[0] == float('inf'):
            return ""
        else:
            return s[ans[1]: ans[2]+1]

s = "ADOBECODEBANC"
t = "ABC"
print(Solution().minWindow(s, t))

s = "a"
t = "a"
print(Solution().minWindow(s, t))

s = "a"
t = "aa"
print(Solution().minWindow(s, t))
