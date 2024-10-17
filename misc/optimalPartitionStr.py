class Solution:
    def partitionString(self, s: str) -> int:
        count = 0
        seen = list()
        for ch in s:
            if ch not in seen:
                seen.append(ch)
            else:
                # ans.append("".join(seen))
                count += 1
                seen = list()
                seen.append(ch)
        if len(seen) > 0:
            # ans.append("".join(seen))
            count += 1

        return count


s = "abacaba"
print(Solution().partitionString(s))

s = "ssssss"
print(Solution().partitionString(s))
