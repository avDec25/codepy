from typing import List


class Solution:
    # Function to detect cycle in a directed graph.
    def hasCycle(self, v: int, adj: List[List[int]], visited: List[bool],
                 rec_stk: List[bool]) -> bool:
        if not visited[v]:
            visited[v] = True
            rec_stk[v] = True
            for neighbour in adj[v]:
                if not visited[neighbour] and self.hasCycle(neighbour, adj, visited, rec_stk):
                    return True
                elif rec_stk[neighbour]:
                    return True
        rec_stk[v] = False
        return False

    def isCyclic(self, V: int, adj: List[List[int]]) -> bool:
        visited = [False] * V
        rec_stk = [False] * V

        for v in range(V):
            if self.hasCycle(v, adj, visited, rec_stk):
                return True
        return False


if __name__ == '__main__':
    V = 5
    adj = [[] for _ in range(V)]
    adj[0].append(1)
    adj[0].append(2)
    adj[1].append(2)
    adj[2].append(3)
    adj[2].append(4)
    adj[4].append(3)
    adj[4].append(0)
    if Solution().isCyclic(V, adj):
        print("contains cycle")
    else:
        print("NO cycle")
