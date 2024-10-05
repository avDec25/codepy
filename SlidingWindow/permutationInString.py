import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s2n = len(s2)
        s1n = len(s1)

        if s2n < s1n:
            return False

        freq = collections.Counter(s1)

        for i in range(s2n):
            counter = collections.Counter(s2[i:i+len(s1)])
            if len(counter.keys()) == len(freq.keys()):
                failed = False
                for key in freq.keys():
                    if counter[key] != freq[key]:
                        failed = True
                        break
                if not failed:
                    return True
        return False


s1 = "hello"
s2 = "ooolleoooleh"
print(Solution().checkInclusion(s1, s2))

s1 = "ab"
s2 = "eidbaooo"
print(Solution().checkInclusion(s1, s2))

s1 = "adc"
s2 = "dcda"
print(Solution().checkInclusion(s1, s2))

s1 = "ab"
s2 = "eidboaoo"
print(Solution().checkInclusion(s1, s2))
