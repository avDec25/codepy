from collections import defaultdict, deque
from typing import List


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(list)
        in_degree = {c: 0 for word in words for c in word}

        for a, b in zip(words, words[1:]):
            for c1, c2 in zip(a, b):
                if c1 != c2:
                    graph[c1].append(c2)
                    in_degree[c2] += 1
                    break
                else:
                    # longer word comes before
                    if len(a) > len(b): # totally invalid, longer word is prefix of shorter
                        return ""


        # khan's algorithm: Topological sorting
        order = []
        q = deque(c for c, deg in in_degree.items() if deg == 0)
        while q:
            c = q.popleft()
            order.append(c)

            for nei in graph[c]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)

        return "".join(order)


print(Solution().foreignDictionary(["hrn", "hrf", "er", "enn", "rfnn"]))
#  this is what zip does
# "hrn"  "hrf" "er"  "enn"
# "hrf"  "er"  "enn" "rfnn"



