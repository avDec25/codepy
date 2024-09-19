from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            a = x + y
            b = y + x
            return int(a) < int(b)

        nstr = [str(x) for x in nums]
        n = len(nstr)
        for i in range(n):
            for j in range(i + 1, n):
                if compare(nstr[i], nstr[j]):
                    temp = nstr[i]
                    nstr[i] = nstr[j]
                    nstr[j] = temp
        return str(int(''.join(nstr)))


nums = [10, 2]
print(Solution().largestNumber(nums))

nums = [3, 31, 30, 34, 5, 9]
print(Solution().largestNumber(nums))
