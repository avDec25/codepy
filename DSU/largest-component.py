from collections import defaultdict
from typing import List
import math


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1 for _ in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        self.size[rx] += self.size[ry]
        return True


class Solution_TLE:
    def largestComponentSize(self, nums: List[int]) -> int:
        n = len(nums)
        uf = UnionFind(n)

        def is_connected(id1, id2):
            return math.gcd(nums[id1], nums[id2]) != 1

        for i in range(n):
            for j in range(i + 1, n):
                if is_connected(i, j):
                    uf.union(i, j)
        return max(uf.size)


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        uf = UnionFind(max(nums) + 1)

        for num in nums:
            val = num
            factor = 2
            while factor ** 2 <= val:
                if val % factor == 0:
                    uf.union(num, factor)
                while val % factor == 0:
                    val //= factor
                factor += 1
            if val > 1:
                uf.union(num, val)

        counts = defaultdict(int)
        mx_size = 0
        for num in nums:
            root = uf.find(num)
            counts[root] += 1
            mx_size = max(mx_size, counts[root])
        return mx_size


nums = [4, 6, 15, 35]
print(Solution().largestComponentSize(nums))

nums = [20, 50, 9, 63]
print(Solution().largestComponentSize(nums))

nums = [2, 3, 6, 7, 4, 12, 21, 39]
print(Solution().largestComponentSize(nums))
