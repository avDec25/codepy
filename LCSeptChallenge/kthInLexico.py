class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def countNumsWithPrefix(curr, n):
            fn = curr
            nn = curr + 1
            total = 0
            while fn <= n:
                total += min(n + 1, nn) - fn
                fn *= 10
                nn *= 10
            return total

        curr = 1
        k -= 1

        while k > 0:
            count = countNumsWithPrefix(curr, n)
            if k >= count:
                curr += 1  # move to next prefix
                k -= count
            else:
                curr *= 10  # go deeper into current
                k -= 1
        return curr


n = 681692778
k = 351251360
print(Solution().findKthNumber(n, k))
