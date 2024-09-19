class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = ""
        for e in s:
            if e.isalpha() or e.isdigit():
                if e.isupper():
                    str += e.lower()
                else:
                    str += e
        # print(str)
        for i in range(len(str)//2):
            if str[i] != str[-(1 + i)]:
                return False
        return True


s = "0P"
print(Solution().isPalindrome(s))

s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))
s = "race a car"
print(Solution().isPalindrome(s))
s = " "
print(Solution().isPalindrome(s))
