from typing import List
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_count = Counter(tasks)
        mx_freq = max(tasks_count.values())
        mx_freq_count = sum(1 for count in tasks_count.values() if count == mx_freq)
        formula_result = (mx_freq-1) * (n+1) + mx_freq_count
        return max(formula_result, len(tasks))




tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
print(Solution().leastInterval(tasks, n))

tasks = ["A", "C", "A", "B", "D", "B"]
n = 1
print(Solution().leastInterval(tasks, n))

tasks = ["A", "A", "A", "B", "B", "B"]
n = 3
print(Solution().leastInterval(tasks, n))
