from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        required = len(need)
        left, right, formed = 0, 0, 0
        have = {}
        ans = (float('inf'), None, None)
        
        while right < len(s):
            # absorb the new character -----------------------------------
            char_right = s[right]
            have[char_right] += 1
            
            if char_right in need and need[char_right] == have[char_right]:
                formed += 1
            
            # until we continue to have all required ---------------------
            while left <= right and formed == required:
                # update ans
                win_size = right - left + 1
                if win_size < ans[0]:
                    ans = (win_size, left, right)
                
                # remove character from window
                left += 1
                char_left = s[left]
                have[char_left] -= 1
                if char_left in need and have[char_left] < need[char_left]:
                    formed -= 1
            
            right += 1
        
        if ans[0] == float('inf'):
            return ""    
        else:
            return s[ans[1]: ans[2]+1]
                

s = "ADOBECODEBANC", t = "ABC"
print(Solution().minWindow(s, t))

s = "a", t = "a"
print(Solution().minWindow(s, t))

s = "a", t = "aa"
print(Solution().minWindow(s, t))
