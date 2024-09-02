from typing import List, Set


def dfs(node: int, adj: List[List[int]], stk: List[int], visited: Set[int]):
    visited.add(node)
    for neighbour in adj[node]:
        if neighbour not in visited:
            dfs(neighbour, adj, stk, visited)
    stk.append(node)


def topologicalSort(V: int, adj: List[List[int]]):
    stk = []
    visited = set()
    for node in range(V):
        if node not in visited:
            dfs(node, adj, stk, visited)

    return stk[::-1]


if __name__ == '__main__':
    V = 7
    adj = [[] for _ in range(V)]
    adj[0].append(1)
    adj[0].append(2)
    adj[1].append(2)
    adj[1].append(5)
    adj[2].append(3)
    adj[5].append(3)
    adj[5].append(4)
    adj[6].append(1)
    adj[6].append(5)
    print(topologicalSort(V, adj))