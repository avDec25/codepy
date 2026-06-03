class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0 for _ in range(n)]

    def find(self, x):
        if self.partent[x] != x:
            # the recursive call goes all the way to the root
            self.parent[x] = self.find(self.parent[x]) # also doing path compression
        return self.parent[x]

    # def union(self, x, y):
    #     rx, ry = self.find(x), self.find(y)
    #     if rx == ry:
    #         return False
    #     if self.rank[rx] < self.rank[ry]:
    #         rx, ry = ry, rx
    #     self.parent[ry] = rx
    #     if self.rank[rx] == self.rank[ry]:
    #         self.rank[rx] += 1
    #     return True

    # Union by Rank
    # rank is an upper bound on height not an exact count
    # path compression flattens tree, but rank never decreases
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)

        if rx == ry:  # already connected
            return False

        # KEEP y small, it connects TO

        # ry will represent the small tree
        # it is always the one that gets under, in next statement
        # so if ry is larger, then swap variable value
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx

        # because we have written the below invariant code
        # (i.e. without if else for which tree is small or large)
        # therefore, we need to have previous statements take care of that
        # to make the correct thing happen
        # which is smaller tree is connected to larger
        # now according to this ry always need to be the smaller tree
        # so check if ry one was larger, if yes then swap variables
        self.parent[ry] = rx # parent of ry is rx now, rx is bigger; Perform Union
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)
