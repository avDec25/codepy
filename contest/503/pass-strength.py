class Solution:
    def passwordStrength(self, password: str) -> int:
        ans = 0
        password = set(password)
        for e in password:
            if 'a' <= e <= 'z':
                ans += 1
            elif 'A' <= e <= 'Z':
                ans += 2
            elif '0' <= e <= '9':
                ans += 3
            elif e in ['!', '@', '#', '$']:
                ans += 5
        return ans

password = "aA1!"
print(Solution().passwordStrength(password))

password = "bbB11#"
print(Solution().passwordStrength(password))
