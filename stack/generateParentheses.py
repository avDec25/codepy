from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def dfs(left, right, s):
            if len(s) == n * 2:
                ans.append(s)

            if left < n:
                dfs(left + 1, right, s + "(")

            if right < left:
                dfs(left, right + 1, s + ")")

        dfs(0, 0, "")
        return ans


n = 1
print(Solution().generateParenthesis(n))

n = 3
print(Solution().generateParenthesis(n))
