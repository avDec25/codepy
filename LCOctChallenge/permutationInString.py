import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = collections.Counter(s1)
        for i in range(len(s2)):
            if s2[i] in counter.keys():
                if counter == collections.Counter(s2[i:i+len(s1)]):
                    return True
        return False

s1 = "ab"
s2 = "eidbaooo"
print(Solution().checkInclusion(s1, s2))

s1 = "ab"
s2 = "eidboaoo"
print(Solution().checkInclusion(s1, s2))
