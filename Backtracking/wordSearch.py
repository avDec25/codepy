from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])

        def backtrack(i, j, wi):
            if wi == len(word):
                return True

            if 0 > i or i >= R or 0 > j or j >= C or board[i][j] != word[wi]:
                return False

            temp = board[i][j]
            board[i][j] = ''
            if backtrack(i + 1, j, wi + 1) \
                    or backtrack(i, j + 1, wi + 1) \
                    or backtrack(i - 1, j, wi + 1) \
                    or backtrack(i, j - 1, wi + 1):
                return True
            board[i][j] = temp
            return False

        for i in range(R):
            for j in range(C):
                if backtrack(i, j, 0):
                    return True

        return False


board = [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]]
word = "AAB"
print(Solution().exist(board, word))

board = [["a", "a"]]
word = "a"
print(Solution().exist(board, word))

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
print(Solution().exist(board, word))

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "SEE"
print(Solution().exist(board, word))

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCB"
print(Solution().exist(board, word))
