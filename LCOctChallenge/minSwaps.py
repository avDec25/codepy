class Solution:
    def minSwaps(self, s: str) -> int:
        ans = 0
        for x in s:
            if x == '[':
                ans += 1
            elif ans > 0:
                ans -= 1
        return (ans + 1) // 2


s = "][]["
print(Solution().minSwaps(s))

s = "]]][[["
print(Solution().minSwaps(s))

s = "[]"
print(Solution().minSwaps(s))
