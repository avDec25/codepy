class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = []

        for char in s:
            if not stk:
                stk.append((char, 1))
                continue
            if stk[-1][0] == char:
                e, c = stk.pop()
                stk.append((e,c+1))
                if stk[-1][1] == k:
                    stk.pop()
            else:
                stk.append((char, 1))

        return "".join(te*c for te, c in stk)


s = "abcd"
k = 2
print(Solution().removeDuplicates(s, k))

s = "deeedbbcccbdaa"
k = 3
print(Solution().removeDuplicates(s, k))

s = "pbbcggttciiippooaais"
k = 2
print(Solution().removeDuplicates(s, k))
