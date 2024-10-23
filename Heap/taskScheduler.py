import collections
import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        mx_freq = max(counter.values())
        mx_freq_counts = sum(1 for count in counter.values() if count == mx_freq)

        heap = []
        for key in counter.keys():
            heapq.heappush(heap, (counter[key], key))

        while len(heap) > 1:




tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
print(Solution().leastInterval(tasks, n))

tasks = ["A", "C", "A", "B", "D", "B"]
n = 1
print(Solution().leastInterval(tasks, n))

tasks = ["A", "A", "A", "B", "B", "B"]
n = 3
print(Solution().leastInterval(tasks, n))
