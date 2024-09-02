from collections import deque


class Solution:
    # 1) can also be solved by Sorting
    # 2) can also be solved by Hashing
    # 3) Solution by Graph, largest set of connected components
    def findLongestConseqSubseq(self, a, N):
        adj = {}
        for r in range(N):
            adj[a[r]] = []
            for c in range(N):
                if abs(a[r] - a[c]) == 1:
                    adj[a[r]].append(a[c])

        lcss = 0
        visited = set()
        q = deque()
        for e in a:
            data = 0
            if e not in visited:
                q.append(e)
                visited.add(e)
                data = data + 1
                while q:
                    popped = q.popleft()
                    for neighbour in adj[popped]:
                        if neighbour not in visited:
                            q.append(neighbour)
                            visited.add(neighbour)
                            data = data + 1

                lcss = max(lcss, data)

        return lcss


n = 7
nodes = [0, 1, 1, 1, 1, 1, 2]
print(Solution().findLongestConseqSubseq(nodes, n))
