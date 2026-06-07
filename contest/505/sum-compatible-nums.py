class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        lo = max(1, n - k)
        hi = n + k

        BITS = 20
        complement = (~n) & ((1 << BITS) - 1)

        total = 0
        mask = complement
        while mask > 0:
            if lo <= mask <= hi:
                total += mask
            mask = (mask - 1) & complement

        return total


n = 2
k = 3
print(Solution().sumOfGoodIntegers(n, k))

n = 5
k = 1
print(Solution().sumOfGoodIntegers(n, k))

n = 1
k = 13
print(Solution().sumOfGoodIntegers(n, k))  # 56
