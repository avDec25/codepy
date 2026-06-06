from collections import defaultdict
from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = defaultdict(str)
        size = defaultdict(int)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            if size[rx] < size[ry]:
                rx, ry = ry, rx

            parent[ry] = rx
            size[rx] += size[ry]

            return True

        for equation in equations:
            for a in (equation[0], equation[-1]):
                if a not in parent:
                    parent[a] = a
                    size[a] += 1

        for equation in equations:
            if equation.find("==") != -1:
                union(equation[0], equation[-1])

        for equation in equations:
            if equation.find("!=") != -1:
                if find(equation[0]) == find(equation[-1]):
                    return False

        return True


equations = ["a==b", "b!=a"]
print(Solution().equationsPossible(equations))

equations = ["b==a", "a==b"]
print(Solution().equationsPossible(equations))

equations = ["c==c", "b==d", "x!=z"]
print(Solution().equationsPossible(equations))
