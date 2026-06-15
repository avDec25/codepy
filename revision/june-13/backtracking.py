from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(i, so_far):
            if i == len(nums):
                ans.append(so_far.copy())
                return

            so_far.append(nums[i])
            backtrack(i + 1, so_far)
            so_far.pop()
            backtrack(i + 1, so_far)

        backtrack(0, [])
        return ans

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        used = set()

        def backtrack(path):
            if len(path) == len(nums):
                ans.append(path.copy())
                return

            for num in nums:
                if num not in used:
                    used.add(num)

                    path.append(num)
                    backtrack(path)
                    path.pop()
                    backtrack(path)

                    used.remove(num)

        backtrack([])
        return ans

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(path, index, k):
            if k < 0:
                return
            if k == 0:
                ans.append(path.copy())
                return

            for i in range(index, len(candidates)):
                path.append(candidates[i])
                backtrack(path, i, k - candidates[i])
                path.pop()

        backtrack([], 0, target)
        return ans

    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [['.' for _ in range(n)] for _ in range(n)]

        def is_safe(r, c):
            for j in range(c - 1, -1, -1):
                if board[r][j] == 'Q':
                    return False

            i = r - 1
            j = c - 1
            while 0 <= i and 0 <= j:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            i = r + 1
            j = c - 1
            while i < n and 0 <= j:
                if board[i][j] == 'Q':
                    return False
                i += 1
                j -= 1

            return True

        def backtrack(col):
            if col >= n:
                ans.append(["".join(row) for row in board])
                return

            for i in range(n):
                if is_safe(i, col):
                    board[i][col] = 'Q'
                    backtrack(col + 1)
                    board[i][col] = '.'

        backtrack(0)
        return ans

    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        if not board or rows == 0 or cols == 0:
            return

        def inRow(num, r, c):
            for i in range(9):
                if board[i][c] == num:
                    return True
            return False

        def inCol(num, r, c):
            for i in range(9):
                if board[r][i] == num:
                    return True
            return False

        def inBox(num, r, c):
            for i in range(3 * (r // 3), 3 * (r // 3) + 3):
                for j in range(3 * (c // 3), 3 * (c // 3) + 3):
                    if board[i][j] == num:
                        return True
            return False

        def backtrack(r, c):
            if c == cols:
                c = 0
                r += 1
            if r == rows:
                return True

            if board[r][c] == '.':
                for num in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    if not inRow(num, r, c) and not inCol(num, r, c) and not inBox(num, r, c):
                        board[r][c] = num
                        if backtrack(r, c + 1):
                            return True
                        board[r][c] = '.'
            else:
                return backtrack(r, c + 1)

        backtrack(0, 0)


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
Solution().solveSudoku(board)
for row in board:
    print(row)
