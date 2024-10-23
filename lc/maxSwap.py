class Solution:
    def maximumSwap(self, num: int) -> int:
        a = list(str(num))
        last_occ = {}

        for i, d in enumerate(a):
            last_occ[int(d)] = i

        for i, x in enumerate(a):
            for d in range(9, int(x), -1):
                if last_occ.get(d, -1) > i:
                    a[i], a[last_occ[d]] = a[last_occ[d]], a[i]
                    return int(''.join(a))

        return num


num = 2736
print(Solution().maximumSwap(num))

num = 98368
print(Solution().maximumSwap(num))

num = 2736
print(Solution().maximumSwap(num))

num = 9973
print(Solution().maximumSwap(num))
