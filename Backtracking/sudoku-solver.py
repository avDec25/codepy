from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])

        if board is None or row == 0 or col == 0:
            return

        def isValid(r, c, x):
            for i in range(9):
                if board[r][i] == x:
                    return False

                if board[i][c] == x:
                    return False

                if board[3 * (r // 3) + i // 3][3 * (c // 3) + i % 3] == x:
                    return False

            return True

        def solve(board):
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        for x in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                            if isValid(r, c, x):
                                board[r][c] = x
                                if solve(board): return True
                                board[r][c] = '.'
                        return False
            return True

        solve(board)


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
Solution().solveSudoku(board)
for row in board:
    print(row)
