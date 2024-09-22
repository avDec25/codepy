class Solution:
    def kmp(self, txt: str, patt: str) -> int:
        new_string = patt + '#' + txt
        print(new_string)
        pi = [0] * len(new_string)
        i = 1
        k = 0
        while i < len(new_string):
            if new_string[i] == new_string[k]:
                k += 1
                pi[i] = k
                i += 1
            else:
                if k > 0:
                    k = pi[k - 1]
                else:
                    pi[i] = 0
                    i += 1
        return pi[-1]

    def shortestPalindrome(self, s: str) -> str:
        count = self.kmp(s[::-1], s)
        print(s, s[::-1], count)
        print(f"{s[count:][::-1]}")
        return s[count:][::-1] + s


s = "aabba"
print(Solution().shortestPalindrome(s))

# s = "ddbkxzx"
# print(Solution().shortestPalindrome(s))
# #
# s = "aacecaaa"
# print(Solution().shortestPalindrome(s))
#
# s = "abcd"
# print(Solution().shortestPalindrome(s))
