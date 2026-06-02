from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def pgen(curr, left, right):
            if len(curr) == 2 * n:
                ans.append(curr)
                return

            if left < n:
                pgen(curr + '(', left + 1, right)

            if right < left:
                pgen(curr + ')', left, right + 1)

        ans = []
        pgen("", 0, 0)
        return ans


n = 1
print(Solution().generateParenthesis(n))

n = 2
print(Solution().generateParenthesis(n))

n = 3
print(Solution().generateParenthesis(n))
