def dfs(node, dest, adj, visited):
    return


def findSCC(self, V, edges):
    graph = [[] for _ in range(V)]
    graphT = [[] for _ in range(V)]
    time = [0 for _ in range(V)]

    for u, v in edges:
        graph[u].append(v)
        graphT[v].append(u)

    visited = set()



if __name__ == '__main__':
    V = 5
edges = [
    (1, 3),
    (1, 4),
    (2, 1),
    (3, 2),
    (4, 5)
]

print(findSCC(V, edges))
