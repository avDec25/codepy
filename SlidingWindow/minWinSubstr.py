import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        counter = collections.Counter(t)
        iterate = []
        for l in range(len(s)):
            if s[l] in t:
                iterate.append(l)

        def all_covered(i):
            freq = collections.defaultdict(int)
            for j in range(i, len(iterate)):
                freq[s[iterate[j]]] += 1
                if len(counter.keys()) == len(freq.keys()):
                    covered = True
                    for key in counter.keys():
                        if counter[key] > freq[key]:
                            covered = False
                            break
                    if covered:
                        return iterate[j]
            return -1

        ans = float('inf')
        substr = ""

        for index, l in enumerate(iterate):
            if s[l] in t:
                r = all_covered(index)
                if r == -1:
                    break
                else:
                    if (r - l + 1) < ans:
                        ans = r - l + 1
                        substr = s[l:r + 1]
                        # print(l, r)
                        # print(substr)

        return substr



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
