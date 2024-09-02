from typing import List


class Solution:
    def construct2DArray(self, a: List[int], m: int, n: int) -> List[List[int]]:
        if len(a) == m * n:
            a_cols = []
            k = 0
            for i in range(m):
                a_row = []
                for j in range(n):
                    a_row.append(a[k])
                    k += 1
                a_cols.append(a_row)
            return a_cols
        else:
            return []


original = [1, 2, 3, 4]
m = 2
n = 2
print(Solution().construct2DArray(original, m, n))
