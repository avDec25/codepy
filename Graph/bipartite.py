from collections import deque


def isBipartite(V, adj):
    q = deque()
    color = [-1 for _ in range(V)]
    for v in range(V):
        if color[v] == -1:
            q.append(v)
            color[v] = 0  # Any default color to begin with
            while q:
                popped = q.popleft()
                for neighbour in adj[popped]:
                    if color[neighbour] == -1:
                        color[neighbour] = 1 - color[popped]
                        q.append(neighbour)
                    if color[neighbour] == color[popped]:
                        return False

    for v in range(V):
        print(f"{v} = {color[v]}")
    return True


if __name__ == '__main__':
    V = 6
    adj = [[] for _ in range(V)]
    adj[0].append(1)
    adj[0].append(4)
    # adj[0].append(3)
    adj[1].append(0)
    adj[1].append(3)
    adj[1].append(2)
    adj[2].append(1)
    adj[3].append(1)
    adj[3].append(4)
    adj[4].append(0)
    adj[4].append(5)
    adj[5].append(4)
    if isBipartite(V, adj):
        print("Is a bipartite graph")
    else:
        print("Is not a bipartite graph")
