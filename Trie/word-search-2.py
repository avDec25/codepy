from collections import deque
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end_of_word = True
        curr.word = word

    def search(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_end_of_word

    def starts_with(self, prefix):
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        trie = Trie()
        for word in words:
            trie.insert(word)

        rows = len(board)
        cols = len(board[0])

        def backtrack(i, j, parent):
            char = board[i][j]
            current_node = parent.children[char]

            if current_node.word is not None:
                ans.append(current_node.word)
                current_node.word = None

            board[i][j] = '#' # marked as visited
            for nx, ny in [
                (i + 1, j),
                (i - 1, j),
                (i, j + 1),
                (i, j - 1)
            ]:
                if 0 <= nx < rows and 0 <= ny < cols:
                    if board[nx][ny] in current_node.children:
                        backtrack(nx, ny, current_node)
            board[i][j] = char

            # Only optimization
            # if current_node has no children then no meaning to maintain the path
            if not current_node.children:
                parent.children.pop(char)

        ans = []
        for i in range(rows):
            for j in range(cols):
                char = board[i][j]
                if char in trie.root.children:
                    backtrack(i, j, trie.root)
        return ans


board = [["o", "a", "a", "n"],
         ["e", "t", "a", "e"],
         ["i", "h", "k", "r"],
         ["i", "f", "l", "v"]]
words = ["oath", "pea", "eat", "rain"]
print(Solution().findWords(board, words))

board = [["a", "b"],
         ["c", "d"]]
words = ["abcb"]
print(Solution().findWords(board, words))
