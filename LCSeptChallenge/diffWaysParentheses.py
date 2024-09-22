from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ans = []
        for i in range(len(expression)):
            op = expression[i]
            if op in ['+', '-', '*']:
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])
                for l in left:
                    for r in right:
                        if op == '+':
                            ans.append(int(l) + int(r))
                        elif op == '-':
                            ans.append(int(l) - int(r))
                        elif op == '*':
                            ans.append(int(l) * int(r))
        if len(ans) == 0:
            ans.append(int(expression))

        return ans


s = "2-1-1"
print(Solution().diffWaysToCompute(s))

s = "2*3-4*5"
print(Solution().diffWaysToCompute(s))
