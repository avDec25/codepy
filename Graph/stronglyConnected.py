from heapq import heappush, heappop


class Time:
    def __init__(self, index, finished):
        self.index = index
        self.finished = finished

    def __repr__(self):
        return f"({self.index}, {self.finished})"

    def __lt__(self, other):
        return self.finished > other.finished


def dfs(node, visited, adj, nodeFT, doPrint):
    global currTime
    if node not in visited:
        visited.add(node)
        for neighbor in adj[node]:
            if neighbor not in visited:
                dfs(neighbor, visited, adj, nodeFT, doPrint)
                currTime += 1

    heappush(nodeFT, Time(node, currTime))
    if doPrint:
        print(node)


def findSCC(V, adj, nodeFT, doPrint):
    global currTime
    visited = set()

    for v in range(1, V):
        if v not in visited:
            dfs(v, visited, adj, nodeFT, doPrint)
            currTime += 1





if __name__ == '__main__':
    V = 6
    adj = [[] for _ in range(V)]
    adjR = [[] for _ in range(V)]

    adj[1].append(3)
    adjR[3].append(1)

    adj[1].append(4)
    adjR[4].append(1)

    adj[2].append(1)
    adjR[1].append(2)

    adj[3].append(2)
    adjR[2].append(3)

    adj[4].append(5)
    adjR[5].append(4)

    currTime = 1
    nodeFT = []
    findSCC(V, adj, nodeFT, False)

    nodeRFT = []
    visited = set()
    while nodeFT:
        popped = heappop(nodeFT)
        if popped.index not in visited:
            dfs(popped.index, visited, adjR, nodeRFT, True)
            print("============")

    while nodeRFT:
        popped = heappop(nodeRFT)
        print(popped)
