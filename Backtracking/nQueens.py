from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = list()
        board = [['.' for _ in range(n)] for _ in range(n)]

        # column by column we try to put Queens, so that is why:
        # parameter of backtrack is col, and
        # we check only left row, top left diagonal, bottom left diagonal to be safe
        def isSafe(r, c):
            # left row check
            for j in range(c):
                if board[r][j] == 'Q':
                    return False

            # upper left diagonal
            i, j = r - 1, c - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i, j = i - 1, j - 1

            # bottom left diagonal
            i, j = r + 1, c - 1
            while i < n and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i, j = i + 1, j - 1

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
