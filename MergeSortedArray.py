from typing import List


class Solution:
    def mergev2(self, a: List[int], m: int, b: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        f = []
        i = 0
        j = 0
        k = 0
        while i < m and j < n:
            if a[i] < b[j]:
                f.append(a[i])
                i += 1
            else:
                f.append(b[j])
                j += 1
            k += 1
        while i < m:
            f.append(a[i])
            i += 1
        while j < n:
            f.append(b[j])
            j += 1

        for k in range(len(f)):
            a[k] = f[k]

    def merge(self, a: List[int], m: int, b: List[int], n: int) -> None:
        k = m+n-1
        i = m-1
        j = n-1
        while i >= 0 and j >= 0:
            if a[i] >= b[j]:
                a[k] = a[i]
                i -= 1
            else:
                a[k] = b[j]
                j -= 1
            k -= 1

        while i >= 0:
            a[k] = a[i]
            k -= 1
            i -= 1

        while j >= 0:
            a[k] = b[j]
            k -= 1
            j -= 1


a = [1,2,3,0,0,0]
m = 3
b = [2,5,6]
n = 3
Solution().merge(a, m, b, n)
print(a)
