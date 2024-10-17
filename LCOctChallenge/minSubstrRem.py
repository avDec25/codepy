class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for ch in s:
            if stack and ch == 'B':
                if stack[-1] == 'A':
                    stack.pop()
                    continue

            if stack and ch == 'D':
                if stack[-1] == 'C':
                    stack.pop()
                    continue

            stack.append(ch)

        return len(stack)

    def minLength_v1(self, s: str) -> int:
        AB = "AB"
        CD = "CD"

        while s.find(AB) > -1 or s.find(CD) > -1:
            s = s.replace(AB, '')
            s = s.replace(CD, '')

        return len(s)


s = "ABFCACDB"
print(Solution().minLength(s))

s = "ACBBD"
print(Solution().minLength(s))
