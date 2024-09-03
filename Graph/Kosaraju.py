def dfs(node, adj, visited, stk):
    if node not in visited:
        visited.add(node)
        for neighbour in adj[node]:
            dfs(neighbour, adj, visited, stk)
        stk.append(node)


def kosarajuPass1(V, adj):
    visited = set()
    stk = []
    for i in range(1, V):
        if i not in visited:
            dfs(i, adj, visited, stk)
    return stk


def kosarajuPass2(stkFT, adj):
    ans = []
    visited = set()
    for v in stkFT[::-1]:
        scc = []
        if v not in visited:
            dfs(v, adj, visited, scc)
        if scc:
            ans.append(scc)
    return ans


if __name__ == '__main__':
    V = 12
    adj = [[] for _ in range(V)]
    adjR = [[] for _ in range(V)]

    adj[1].append(2)
    adjR[2].append(1)

    adj[2].append(3)
    adjR[3].append(2)

    adj[2].append(4)
    adjR[4].append(2)

    adj[3].append(1)
    adjR[1].append(3)

    adj[4].append(5)
    adjR[5].append(4)

    adj[5].append(6)
    adjR[6].append(5)

    adj[6].append(4)
    adjR[4].append(6)

    adj[7].append(6)
    adjR[6].append(7)

    adj[7].append(8)
    adjR[8].append(7)

    adj[8].append(9)
    adjR[9].append(8)

    adj[9].append(10)
    adjR[10].append(9)

    adj[10].append(7)
    adjR[7].append(10)

    adj[10].append(11)
    adjR[11].append(10)

    stackByStartTime = kosarajuPass1(V, adj)
    print(stackByStartTime)

    sccs = kosarajuPass2(stackByStartTime, adjR)
    print(sccs)
