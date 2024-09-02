import heapq


class Solution:
    def findMaxContinuousProduct(self, a, k):
        ans = float('-inf')
        cp = 1
        for i in range(k):
            cp *= a[i]

        ans = max(ans, cp)
        moved_over = 0
        for i in range(k, len(a)):
            cp = cp // a[moved_over]
            moved_over += 1
            cp = cp * a[i]
            ans = max(ans, cp)

        return ans


if __name__ == '__main__':
    a = [10, 2, 3, 10, 5, 1, 4]
    k = 5
    print(Solution().findMaxContinuousProduct(a, k))
