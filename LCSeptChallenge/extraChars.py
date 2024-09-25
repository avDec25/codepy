from typing import List
import re


class Solution:
    def minExtraChar_failed(self, s: str, dictionary: List[str]) -> int:
        prev = [1] * len(s)
        dictionary.sort(key=lambda x: len(x), reverse=True)
        removed = [1] * len(s)
        print(f"{' ' * 5:>5}   {'  '.join(s)}")
        for word in dictionary:
            pp = False
            for i in [m.start() for m in re.finditer(word, s)]:
                if removed[i] != 0 and removed[i + len(word) - 1] != 0:
                    for j in range(i, i + len(word)):
                        removed[j] = 0

            for x in range(len(removed)):
                if prev[x] != removed[x]:
                    prev = removed.copy()
                    pp = True
                    break
            if pp:
                print(f"{word:>5}: {removed}")
        return sum(removed)

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dictionary = set(dictionary)

        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1] + 1
            for j in range(i, n):
                substr = s[i:j + 1]
                if substr in dictionary:
                    dp[i] = min(dp[i], dp[j + 1])
        return dp[0]


s = "rkmsilizktprllwoimafyuqmeqrujxdzgp"
dictionary = ["afy", "lyso", "ymdt", "uqm", "cfybt", "lwoim", "hdzeg", "th",
              "rkmsi", "d", "e", "tp", "r", "jx", "tofxe", "etjx", "llqs",
              "cpir", "p", "ncz", "ofeyx", "eqru", "l", "demij", "tjky",
              "jgodm", "y", "ernt", "jfns", "akjtl", "wt", "tk", "zg", "lxoi",
              "kt"]
print(Solution().minExtraChar(s, dictionary))

# s = "eglglxa"
# dictionary = ["rs", "j", "h", "g", "fy", "l", "fc", "s", "zf", "i", "k", "x",
#               "gl", "qr", "qj", "b", "m", "cm", "pe", "y", "ei", "wg", "e", "c",
#               "ll", "u", "lb", "kc", "r", "gs", "p", "ga", "pq", "o", "wq",
#               "mp", "ms", "vp", "kg", "cu"]
# print(Solution().minExtraChar(s, dictionary))
#
# s = "dwmodizxvvbosxxw"
# dictionary = ["ox", "lb", "diz", "gu", "v", "ksv", "o", "nuq", "r", "txhe", "e",
#               "wmo", "cehy", "tskz", "ds", "kzbu"]
# print(Solution().minExtraChar(s, dictionary))
#
# s = "leetscode"
# dictionary = ["leet", "code", "leetcode"]
# print(Solution().minExtraChar(s, dictionary))
#
# s = "sayhelloworld"
# dictionary = ["hello", "world"]
# print(Solution().minExtraChar(s, dictionary))
