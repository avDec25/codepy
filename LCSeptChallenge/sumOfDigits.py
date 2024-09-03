class Solution:
    def getLucky(self, s: str, k: int) -> int:
        cr = ''.join(str(ord(e) - ord('a') + 1) for e in s)
        sm = sum([int(ch) for ch in cr])

        while k > 1:
            k -= 1
            sod = 0
            while sm > 0:
                sod += sm % 10
                sm //= 10
            sm = sod
        return sm


s = "zbax"
k = 2
print(Solution().getLucky(s, k))
