class Solution:
    def parseBoolExpr(self, exp: str) -> bool:
        exp = list(exp)
        i = 0

        def eval():
            nonlocal i

            c = exp[i]
            i += 1
            if c == 't':
                return True
            if c == 'f':
                return False
            if c == '!':
                i += 1
                res = not eval()
                i += 1
                return res

            children = []
            i += 1
            while exp[i] != ')':
                if exp[i] != ',':
                    children.append(eval())
                else:
                    i += 1

            i += 1
            if c == '&':
                return all(children)

            if c == '|':
                return any(children)

        return eval()


expression = "&(|(f))"
print(Solution().parseBoolExpr(expression))

expression = "|(f,f,f,t)"
print(Solution().parseBoolExpr(expression))

expression = "!(&(f,t))"
print(Solution().parseBoolExpr(expression))
