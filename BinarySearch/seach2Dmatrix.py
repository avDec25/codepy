from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:



matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
Solution().searchMatrix(matrix, target)

matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 13
Solution().searchMatrix(matrix, target)
