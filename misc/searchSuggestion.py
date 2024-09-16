from typing import List


class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.wordEnd = False


def insert(node, key):
    curr = node
    for c in key:
        index = ord(c) - ord('a')
        if curr.child[index] is None:
            curr.child[index] = TrieNode()
        curr = curr.child[index]
    curr.wordEnd = True


def search(node, key):
    curr = node
    for c in key:
        index = ord(c) - ord('a')
        if curr.child[index] is None:
            return False
        curr = curr.child[index]
    return curr.wordEnd


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = TrieNode()
        for word in products:
            insert(root, word)

        ans = []
        for j in range(len(searchWord)):
            key = searchWord[:j]
            if search(root, key):
                print('found')

        return ans




products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
searchWord = "mouse"
print(Solution().suggestedProducts(products, searchWord))

# output = [["mobile", "moneypot", "monitor"],
#           ["mobile", "moneypot", "monitor"],
#           ["mouse", "mousepad"],
#           ["mouse", "mousepad"],
#           ["mouse", "mousepad"]]
