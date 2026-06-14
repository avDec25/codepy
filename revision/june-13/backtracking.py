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
        ans = list()
        board = [['.'] * n for _ in range(n)]

        # > sweep will cover all cells behind
        def isSafe(r, c):
            for j in range(c, -1, -1):
                if board[r][j] == 'Q':
                    return False

            i = r - 1
            j = c - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            i = r + 1
            j = c - 1
            while i < n and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i += 1
                j -= 1

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
