# from collections import Counter
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         if not s or not t:
#             return ""
#         # Count how many times each char appears in t
#         need = Counter(t)
#         # Number of unique characters in t that need to be present in the window
#         required = len(need)
#
#         # Left and Right pointer
#         left, right = 0, 0
#         # How many unique characters in current window satisfy the required count
#         formed = 0
#
#         # Window counts
#         have = {}
#
#         # (window length, left, right) for the best (smallest) window found
#         ans = (float("inf"), None, None)
#
#         # Expand the window with right pointer
#         while right < len(s):
#             char = s[right]
#             have[char] = have.get(char, 0) + 1
#
#             # If this char is one of the needed, and we've now met the needed count, increment formed
#             if char in need and have[char] == need[char]:
#                 formed += 1
#
#             # Try and contract from the left while window is still “desirable” (i.e. contains all needed chars)
#             while left <= right and formed == required:
#                 char_left = s[left]
#
#                 # Update answer if this window is smaller than previous best
#                 window_size = right - left + 1
#                 if window_size < ans[0]:
#                     ans = (window_size, left, right)
#
#                 # Now try to remove s[left] from window and move left ahead
#                 have[char_left] -= 1
#                 if char_left in need and have[char_left] < need[char_left]:
#                     formed -= 1
#
#                 left += 1
#
#             # Expand right
#             right += 1
#
#         # Return the best window substring, or "" if none found
#         if ans[0] == float("inf"):
#             return ""
#         else:
#             _, start, end = ans
#             return s[start: end + 1]


from collections import Counter
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

            if char_right in need and have[char_right] == need[char_right]:
                formed += 1

            while left <= right and formed == required:
                char_left = s[left]
                window_size = right - left + 1
                if window_size < ans[0]:
                    ans = (window_size, left, right)

                have[char_left] -= 1
                if char_left in need and have[char_left] < need[char_left]:
                    formed -= 1
                left += 1

            right += 1

        if ans[0] == float("inf"):
            return ""
        else:
            return s[ans[1]: ans[2]+1]



s = "cabwefgewcwaefgcf"
t = "cae"
print(Solution().minWindow(s, t))

s = "ADOBECODEBANC"
t = "ABC"
print(Solution().minWindow(s, t))

s = "a"
t = "a"
print(Solution().minWindow(s, t))

s = "a"
t = "aa"
print(Solution().minWindow(s, t))
