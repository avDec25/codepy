class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stk = []
        for c in s:
            if c in brackets.keys():
                stk.append(brackets[c])
            else:
                if not stk or stk[-1] != c:
                    return False
                stk.pop()
        return len(stk) == 0


s = "["
print(Solution().isValid(s))
s = "]"
print(Solution().isValid(s))
s = "()"
print(Solution().isValid(s))
s = "()[]{}"
print(Solution().isValid(s))
s = "(]"
print(Solution().isValid(s))
s = "([])"
print(Solution().isValid(s))
