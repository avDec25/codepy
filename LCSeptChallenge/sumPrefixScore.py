import collections
from typing import List


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        def gen_prefixes(word):
            n = len(word)
            ans = []
            for i in range(1, n + 1):
                ans.append(word[:i])
            # print(f"prefixes of {word} = {ans}")
            return ans

        prefixes = dict()
        freq = collections.defaultdict(int)
        for word in words:
            prefixes[word] = gen_prefixes(word)
            for x in prefixes[word]:
                freq[x] += 1

        ans = []
        for word in words:
            temp = 0
            for x in prefixes[word]:
                temp += freq[x]
            ans.append(temp)
        return ans


words = ["abc", "ab", "bc", "b"]
print(Solution().sumPrefixScores(words))

words = ["abcd"]
print(Solution().sumPrefixScores(words))
