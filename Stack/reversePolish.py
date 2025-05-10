from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def add(x, y):
            return x + y

        def subtract(x, y):
            return y - x

        def multiply(x, y):
            return x * y

        def divide(x, y):
            return int(y / x)

        operators = {
            '+': add,
            '-': subtract,
            '*': multiply,
            '/': divide
        }
        stk = []
        for t in tokens:
            if t in operators:
                poped1 = int(stk.pop())
                poped2 = int(stk.pop())
                stk.append(operators[t](poped1, poped2))
            else:
                stk.append(int(t))

        return stk[-1]


tokens = ["2", "1", "+", "3", "*"]
print(Solution().evalRPN(tokens))

tokens = ["4", "13", "5", "/", "+"]
print(Solution().evalRPN(tokens))

tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(Solution().evalRPN(tokens))
