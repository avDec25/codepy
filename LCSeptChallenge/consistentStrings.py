from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        allowed = set(allowed)
        for word in words:
            word = set(word)
            if word.issubset(allowed):
                ans += 1
        return ans


if __name__ == '__main__':
    allowed = "ab"
    words = ["ad", "bd", "aaab", "baa", "badab"]
    print(Solution().countConsistentStrings(allowed, words))

    allowed = "abc"
    words = ["a", "b", "c", "ab", "ac", "bc", "abc"]
    print(Solution().countConsistentStrings(allowed, words))

