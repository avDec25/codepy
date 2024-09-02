class Solution:
    def stringHash(self, s: str, k: int) -> str:
        ans = []
        for i in range(0, len(s), k):
            hash_sum = 0
            for c in s[i:i + k]:
                hash_sum += ord(c) - ord('a')
            hashed_char = hash_sum % 26
            ans.append(chr(hashed_char + ord('a')))
        return "".join(ans)


s = "abcd"
k = 2
print(Solution().stringHash(s, k))
