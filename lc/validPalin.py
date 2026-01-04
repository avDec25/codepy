class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if left < right and s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))

s = "race a car"
print(Solution().isPalindrome(s))

s = " "
print(Solution().isPalindrome(s))
