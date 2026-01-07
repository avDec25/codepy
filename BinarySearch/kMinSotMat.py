from typing import List


# mx_heap = [] # max-heap of k size will have the kth min at top
# merge-sorting: k-sorted arrays insertion in minheap

# binary-search solution
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def count(x: int) -> int:
            ans = 0
            row = n - 1
            col = 0
            while row >= 0 and col < n:
                if matrix[row][col] <= x:
                    ans += (row+1)
                    col += 1
                else:
                    row -= 1
            return ans

        lo = matrix[0][0]
        hi = matrix[n - 1][n - 1]
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            cnt = count(mid)
            if cnt < k:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo


matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = 8
print(Solution().kthSmallest(matrix, k))

matrix = [[-5]]
k = 1
print(Solution().kthSmallest(matrix, k))
