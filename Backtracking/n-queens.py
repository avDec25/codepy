from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = list()
        board = [['.'] * n for _ in range(n)]

        def isSafe(row, col):
            for j in range(col, -1, -1):
                if board[row][j] == 'Q':
                    return False

            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i, j = i-1, j-1

            i, j = row + 1, col - 1
            while i < n and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i, j = i+1, j-1

            return True

        def backtrack(col):
            if col >= n:
                ans.append(["".join(c) for c in board])
                return

            for row in range(n):
                if isSafe(row, col):
                    board[row][col] = 'Q'
                    backtrack(col + 1)
                    board[row][col] = '.'

        backtrack(0)
        return ans


n = 4
print(Solution().solveNQueens(n))
