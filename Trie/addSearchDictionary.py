class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node:
                node[c] = TrieNode()
            node = node[c]
        node.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(node, index):
            if index == len(word):
                return  node.isEnd
            if word[index] == '.':
                for child in node.children.values():
                    if dfs(child, index+1):
                        return True
            if word[index] in node.children:
                return dfs(node.children[word[index]], index+1)

        return dfs(self.root, 0)
