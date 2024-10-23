class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def backtrack(start, seen):
            if start == len(s):
                return 0
            mx_splits = 0
            for end in range(start+1, len(s) + 1):
                sub = s[start:end]
                if sub not in seen:
                    seen.add(sub)
                    mx_splits = max(mx_splits, 1+backtrack(end, seen))
                    seen.remove(sub)
            return mx_splits

        return backtrack(0, set())


s = "ababccc"
print(Solution().maxUniqueSplit(s))

s = "aba"
print(Solution().maxUniqueSplit(s))

s = "aa"
print(Solution().maxUniqueSplit(s))
