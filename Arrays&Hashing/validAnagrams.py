import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cs = collections.Counter(s)
        ct = collections.Counter(t)
        return cs == ct


s = "anagram"
t = "nagaram"
print(Solution().isAnagram(s, t))

s = "rat"
t = "car"
print(Solution().isAnagram(s, t))
