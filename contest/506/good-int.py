class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        sq_sum = 0
        di_sum = 0
        while n:
            rem = n % 10
            sq_sum += rem **2
            di_sum += rem
            n //= 10
        return (sq_sum - di_sum) >= 50

n = 1000
print(Solution().checkGoodInteger(n))

n = 19
print(Solution().checkGoodInteger(n))
