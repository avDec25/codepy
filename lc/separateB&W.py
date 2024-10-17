class Solution:
    def minimumSteps(self, s: str) -> int:
        swap, black = 0, 0
        for c in s:
            if c == '1':
                black += 1
            else:
                swap += black
        return swap


s = "01001010110"
print(Solution().minimumSteps(s))

s = "101"
print(Solution().minimumSteps(s))

s = "100"
print(Solution().minimumSteps(s))

s = "0111"
print(Solution().minimumSteps(s))
