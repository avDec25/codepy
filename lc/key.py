class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        ones = float('inf')
        tens = float('inf')
        hund = float('inf')
        thou = float('inf')
        for num in [num1, num2, num3]:
            ones = min(ones, (num // 1) % 10)
            tens = min(tens, (num // 10) % 10)
            hund = min(hund, (num // 100) % 10)
            thou = min(thou, (num // 1000) % 10)

        return ones + tens * 10 + hund * 100 + thou * 1000


num1 = 987
num1 = 1
num2 = 879
num2 = 10
num3 = 798
num3 = 1000
print(Solution().generateKey(num1, num2, num3))
