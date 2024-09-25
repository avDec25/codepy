import itertools
from typing import List


class TrieNode:
    def __init__(self):
        self.child = [None] * 10


def insert(node, key):
    curr = node
    for c in key:
        index = int(c)
        if curr.child[index] is None:
            curr.child[index] = TrieNode()
        curr = curr.child[index]


def longest_prefix(node, key):
    curr = node
    n = 0
    for c in key:
        index = int(c)
        if curr.child[index]:
            n += 1
            curr = curr.child[index]
        else:
            break
    return n


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = TrieNode()
        for x in arr1:
            insert(trie, str(x))

        lp = 0
        for x in arr2:
            lp = max(lp, longest_prefix(trie, str(x)))
        return lp


arr1 = [1, 10, 100]
arr2 = [1000]
print(Solution().longestCommonPrefix(arr1, arr2))

arr1 = [1, 2, 3]
arr2 = [4, 4, 4]
print(Solution().longestCommonPrefix(arr1, arr2))
