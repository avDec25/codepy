from collections import defaultdict


class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        n = str(n)
        memo = defaultdict(int)
        for c in n:
            memo[c] += 1

        return sum(int(key)*memo[key] for key in memo.keys())


n = 122
print(Solution().digitFrequencyScore(n))