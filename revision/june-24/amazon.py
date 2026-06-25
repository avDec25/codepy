import heapq
from typing import List, Optional
from collections import OrderedDict, Counter, deque, defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)  # made it most recently used
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        for e, f in freq.items():
            heapq.heappush(heap, (f, e))
            if len(heap) > k:
                heapq.heappop(heap)
        return [e for f, e in heap]

    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            grid[r][c] = "0"
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                    dfs(nr, nc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)

        return islands

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        i = 0
        intervals.sort()
        while i < len(intervals):
            s = intervals[i][0]
            e = intervals[i][1]
            while i < len(intervals) - 1 and e >= intervals[i + 1][0]:
                i += 1
                e = max(e, intervals[i][1])
            ans.append([s, e])
            i += 1
        return ans

    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        ans = 0
        for right, e in enumerate(s):
            if e in last_seen and last_seen[e] >= left:
                left = last_seen[e] + 1
            last_seen[e] = right
            ans = max(ans, right - left + 1)
        return ans

    def canFinish_bfs(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0 for _ in range(numCourses)]
        adj = [list() for _ in range(numCourses)]
        for u, v in prerequisites:
            adj[v].append(u)
            in_degree[u] += 1

        q = deque([v for v in range(numCourses) if in_degree[v] == 0])
        finished = 0
        while q:
            n = len(q)
            while n:
                popped = q.popleft()
                finished += 1
                for neighbor in adj[popped]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        q.append(neighbor)
                n -= 1

        return finished == numCourses

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        state = [0 for _ in range(numCourses)]
        adj = [list() for _ in range(numCourses)]
        for u, v in prerequisites:
            adj[v].append(u)

        def has_cycle(node):
            if state[node] == 2:
                return False
            if state[node] == 1:
                return True

            state[node] = 1
            for nei in adj[node]:
                if has_cycle(nei):
                    return True

            state[node] = 2
            return False

        for i in range(numCourses):
            if state[i] == 0:
                if has_cycle(i):
                    return False

        return numCourses == len([1 for i in range(numCourses) if state[i] == 2])

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        ans = []
        while q:
            n = len(q)
            level = []
            while n:
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                n -= 1
            ans.append(level)
        return ans

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i, e in enumerate(nums):
            complement = target - e
            if complement in seen:
                return [seen[complement], i]
            seen[e] = i

        return []

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            anagrams[key].append(word)
        return [value for value in anagrams.values()]

    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        mx = max(freq.values())
        return sum(1 for x in nums if freq[x] == mx)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def approx_distance_to_origin(point):
            return point[0] ** 2 + point[1] ** 2

        heap = []
        for i, point in enumerate(points):
            heapq.heappush(heap, (-approx_distance_to_origin(point), i))
            if len(heap) > k:
                heapq.heappop(heap)

        return [points[i] for _, i in heap]

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        heap = []
        for i, p in enumerate(lists):
            if p:
                heapq.heappush(heap, (p.val, i, p))

        while heap:
            val, i, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
