from typing import List
import bisect


class Solution:
    def searchMatrix(self, a: List[List[int]], target: int) -> bool:
        R = len(a)
        C = len(a[0])

        col = []
        for i in range(R):
            col.append(a[i][0])
        i = bisect.bisect_left(col, target)
        if i < R:
            if a[i][0] == target:
                return True
        j = bisect.bisect_left(a[i-1], target)
        if j < C:
            return a[i-1][j] == target
        else:
            return False


matrix = [[1], [3]]
target = 1
print(Solution().searchMatrix(matrix, target))

matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
print(Solution().searchMatrix(matrix, target))

matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 13
print(Solution().searchMatrix(matrix, target))
