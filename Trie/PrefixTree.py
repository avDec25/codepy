class Trie:
    def __repr__(self):
        ans = []
        for key, val in self.root.items():
            ans.append(f"{key}: {val}")

        return "\n".join(ans)

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['*'] = ''

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c in node:
                node = node[c]
            else:
                return False
        return node['*'] == ''

    def startsWith(self, prefix: str) -> bool:


# ["Trie",  "insert",  "search", "search", "startsWith", "insert", "search"]
# [    [], ["apple"], ["apple"],  ["app"],      ["app"],  ["app"],  ["app"]]

t = Trie()
t.insert("cat")
t.insert("car")
t.insert("card")
t.insert("care")
t.insert("bat")
print(t)
