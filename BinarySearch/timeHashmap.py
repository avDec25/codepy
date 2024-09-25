from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.hash = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        vals = self.hash.get(key, [])
        lo = 0
        hi = len(vals)-1
        ans = ""
        while lo <= hi:
            mid = (lo+hi) //2
            if vals[mid][1] <= timestamp:
                lo = mid + 1
                ans = vals[mid][0]
            else:
                hi = mid-1
        return ans



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)