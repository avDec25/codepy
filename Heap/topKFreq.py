import heapq
from collections import Counter


class HeapNode:
    def __init__(self, e, f):
        self.e = e  # element
        self.f = f  # frequency

    def __lt__(self, other):
        if self.f == other.f:
            return self.e > other.e
        else:
            return self.f > other.f


class Solution:
    def topK(self, a, k):
        ans = []
        heap = []

        freq = Counter(a)
        for key in freq.keys():
            heapq.heappush(heap, HeapNode(key, freq[key]))

        for _ in range(k):
            ans.append(heapq.heappop(heap).e)

        return ans


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(Solution().topK(nums, k))

    nums = [10, 10, 20, 20, 30, 30, 30, 40]
    k = 2
    print(Solution().topK(nums, k))

    nums = [6, 1, 1, 1, 2, 2, 3]
    k = 2
    print(Solution().topK(nums, k))

    nums = [2, 3, 10]
    k = 1
    print(Solution().topK(nums, k))
