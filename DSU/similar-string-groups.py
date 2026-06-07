from typing import List


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        # important to initialize like this because if we do
        # parent = defaultdict(int) then the default value will be 0 for the root
        # so all elements will be inside the same component. Which is totally incorrect
        parent = list(range(len(strs)))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            parent[ry] = rx
            return True

        def is_similar(x, y):
            diff_pos = 0
            for i in range(len(x)):
                if x[i] != y[i]:
                    diff_pos += 1
                    if diff_pos > 2:
                        return False
            return diff_pos == 0 or diff_pos == 2

        components = len(strs)
        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                if is_similar(strs[i], strs[j]):
                    if union(i, j):
                        components -= 1
        return components


strs = ["tars", "rats", "arts", "star"]
print(Solution().numSimilarGroups(strs))

strs = ["omv", "ovm"]
print(Solution().numSimilarGroups(strs))
