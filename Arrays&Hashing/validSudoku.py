from typing import List


class Solution:
    def allRowsValid(self, board):
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in seen:
                        return False
                    else:
                        seen.add(board[i][j])
        return True

    def allColumnsValid(self, board):
        for j in range(9):
            seen = set()
            for i in range(9):
                if board[i][j] != '.':
                    if board[i][j] in seen:
                        return False
                    else:
                        seen.add(board[i][j])
        return True

    def allSubBoxesValid(self, board):
        for R in [(0, 3), (3, 6), (6, 9)]:
            for C in [(0, 3), (3, 6), (6, 9)]:
                seen = set()
                for r in range(R[0], R[1]):
                    for c in range(C[0], C[1]):
                        if board[r][c] != '.':
                            if board[r][c] in seen:
                                return False
                            else:
                                seen.add(board[r][c])
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.allRowsValid(board) and self.allColumnsValid(
            board) and self.allSubBoxesValid(board)


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
print(Solution().isValidSudoku(board))

board = [["8", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
print(Solution().isValidSudoku(board))
