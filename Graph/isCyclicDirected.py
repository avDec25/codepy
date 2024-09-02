from typing import List


class Solution:
    def isCyclic(self, V: int, adj: List[List[int]]) -> bool:
        inDeg = [0] * V

        for v in range(V):
            for neighbour in adj[v]:
                inDeg[neighbour] += 1

        stk = []
        for v in range(V):
            if inDeg[v] == 0:
                stk.append(v)

        visited = set()
        while stk:
            popped = stk.pop()
            visited.add(popped)
            for neighbour in adj[popped]:
                inDeg[neighbour] -= 1
                if inDeg[neighbour] == 0:
                    stk.append(neighbour)

        return len(visited) != V


if __name__ == '__main__':
    V = 6
    adj = [[] for _ in range(V)]
    adj[2].append(3)
    adj[3].append(2)
    adj[4].append(0)
    adj[4].append(1)
    adj[5].append(0)
    adj[5].append(2)
    print(Solution().topologicalSort(V, adj))
    print(Solution().isCyclic(V, adj))
