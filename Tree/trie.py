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


if __name__ == '__main__':

    root = TrieNode()
    arr = ["and", "ant", "do", "geek", "dad", "ball"]
    for s in arr:
        insert(root, s)

    search_keys = ["do", "gee", "bat", "geek"]
    for s in search_keys:
        print(f"Key : {s}", end=' : ')
        if search(root, s):
            print("Present\n")
        else:
            print("Not Present\n")
