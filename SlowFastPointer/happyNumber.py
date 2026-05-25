class Solution:
    def isHappy(self, n: int) -> bool:
        mp = set()
        mp.add(n)
        while True:
            sq_sum = 0
            while n:
                x = n % 10
                n //= 10
                sq_sum += x * x
            n = sq_sum
            # print(n)
            if n == 1:
                return True
            if n in mp:
                return False
            else:
                mp.add(n)


n = 19
print(Solution().isHappy(n))

n = 2
print(Solution().isHappy(n))
