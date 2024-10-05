from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(lo, hi):
            while lo < hi:
                if s[lo] != s[hi]:
                    return False
                lo += 1
                hi -= 1
            return True

        ans = []

        def backtrack(temp, index):
            if len(s) == index:
                ans.append(temp.copy())
                return

            for i in range(index, len(s)):
                if is_palindrome(index, i):
                    temp.append(s[index:i + 1])
                    backtrack(temp, i + 1)
                    temp.pop()

        backtrack([], 0)
        return ans


s = "aab"
print(Solution().partition(s))

s = "a"
print(Solution().partition(s))
